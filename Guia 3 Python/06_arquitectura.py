import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)   
class Inventario_trapiche:
    def __init__(self):
        self.productos : list[dict] = []
    def agregar_lote(self, tipo: str, kilos: float) -> dict:
        lote = {'id': len(self.productos) + 1, 'tipo': tipo, 'kilos': kilos}
        self.productos.append(lote)
        return lote
    def obtener_todos(self) -> list[dict]:
        return self.productos
gestor_inventario = Inventario_trapiche()
@app.route("/api/inventario", methods=["GET"])
def ver_inventario() -> tuple [Response, int]:
    datos = gestor_inventario.obtener_todos()
    return jsonify({"total": len(datos), "lotes": datos}), 200
@app.route("/api/inventario", methods=["POST"])
def registrar_lote() -> tuple [Response, int]:
    try:
        payload = request.get_json()
        nuevo_lote = gestor_inventario.agregar_lote(payload["tipo"], payload["kilos"])
        return jsonify({"mensaje": "Lote registrado exitosamente", "data": nuevo_lote}), 201
    except (KeyError, TypeError):
        return jsonify({"error": "Estructura JSON invalida"}), 400
if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5000)), debug=os.getenv("FLASK_ENV", "False").lower() == "true")