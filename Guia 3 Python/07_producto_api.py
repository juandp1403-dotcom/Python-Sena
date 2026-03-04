import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from dotenv import load_dotenv  
load_dotenv()
app = Flask(__name__)
CORS(app)
class Productos:
    def __init__(self):
        self.productos : list[dict] = []
    def agregar_producto(self, nombre: str, precio: float) -> dict:
        producto = {'id': len(self.productos) + 1, 'nombre': nombre, 'precio': precio}
        self.productos.append(producto)
        return producto
    def obtener_productos(self) -> list[dict]:
        return self.productos
gestor_productos = Productos()
@app.route("/api/productos_api", methods=["GET"])
def ver_productos() -> tuple [Response, int]:
    datos = gestor_productos.obtener_productos()
    return jsonify({"total": len(datos), "productos": datos}), 200
@app.route("/api/productos_api", methods=["POST"])
def registrar_producto() -> tuple [Response, int]:
    try:
        payload = request.get_json()
        nuevo_producto = gestor_productos.agregar_producto(payload["nombre"], payload["precio"])
        return jsonify({"mensaje": "Producto registrado exitosamente", "data": nuevo_producto}), 201
    except (KeyError, TypeError):
        return jsonify({"error": "Estructura JSON invalida"}), 400
if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5000)), debug=os.getenv("FLASK_ENV", "False").lower() == "true")