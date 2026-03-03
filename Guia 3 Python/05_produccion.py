import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)
@app.route("/api/config", methods=["GET"])
def obtener_config():
    ambiente_actual = os.getenv("FLASK_ENV", "Produccion")
    puerto_asignado = os.getenv("PORT", "5000")
    return jsonify({
        "Status" : "Servidor seguro en linea",
        "ambiente": ambiente_actual,
        "puerto": puerto_asignado
    }), 200
if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_ENV", "False").lower() == "true"
    puerto = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto, debug=debug_mode)