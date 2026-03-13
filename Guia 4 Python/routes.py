from flask import Blueprint, request, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, get_jwt_identity
from models import db, Usuario, Producto
api_bp = Blueprint('api', __name__)
@api_bp.route('/usuarios/registrar', methods=['POST'])
def registrar_usuario():
    try:
        payload = request.get_json()
        clave_segura = generate_password_hash(payload['password'])
        nuevo_user = Usuario(username=payload['username'], password_hash=clave_segura, rol=payload.get('rol', 'Operario'))
        db.session.add(nuevo_user)
        db.session.commit()
        return jsonify({'message': 'Usuario registrado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'Fallo de integridad. Error': str(e)}), 400

@api_bp.route('/usuarios', methods=['POST'])
def listar_usuarios() -> tuple[Response, int]:
    pagina = request.args.get('pagina', 1, type=int)
    paginacion = Usuario.query.paginate(page=pagina, per_page=10, error_out=False)
    resultado = [usuario.serializar() for usuario in paginacion.items]
    return jsonify({
        'usuarios': resultado,
        'total': paginacion.total,
        'pagina_actual': paginacion.page
    }), 200
@api_bp.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    usuario = Usuario.query.filter_by(username=payload['username']).first()
    if usuario and check_password_hash(usuario.password_hash, payload['password']):
        token_acceso = create_access_token(
            identity=usuario.username,
            additional_claims={"rol": usuario.rol})
        return jsonify({'message': 'Login exitoso', 'access_token': token_acceso}), 200
    return jsonify({'message': 'Credenciales invalidas'}), 401
@api_bp.route('/inventario/critico', methods=['POST'])
@jwt_required()
def modificar_inventario()-> tuple[Response, int]:
    usuario_actual = get_jwt_identity()
    claims = get_jwt()
    if claims["rol"] != "Administrador":
        return jsonify({
            'error': 'forbidden: Solo administradores pueden modificar el inventario crítico.'
        }), 403
    return jsonify({
                    'message': 'Inventario crítico modificado exitosamente',
                    'operador': usuario_actual
                }), 200