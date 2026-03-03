from flask import Flask,  request, jsonify, Response
app = Flask(__name__)
usuariosdb: list[dict] = []
@app.route("/api/usuarios", methods=["POST"])
def crear_usuario() -> tuple[Response, int]:
    datos_entrantes: dict = request.get_json()
    if not datos_entrantes or "nombre" not in datos_entrantes:
        return jsonify({"error": "Datos incompletos"}), 400
    nuevo_usuario: dict = {
        "id": len(usuariosdb) + 1,
        "nombre": datos_entrantes["nombre"],
        "rol": datos_entrantes.get("rol", "usuario estandar")
    }
    usuariosdb.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado exitosamente", "data": nuevo_usuario}), 201
if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug=True)