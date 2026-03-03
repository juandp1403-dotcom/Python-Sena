from flask import Flask
app = Flask(__name__)
@app.route("/api/saludar/<string:nombre>", methods=["GET"])
def saludar(nombre : str)-> str:
    return f"<h1>Bienvenido al sistema de saludos</h1> <p>Hola {nombre}!Tu solicitud fue enrutada correctamente.</p>"
@app.route("/api/calcular_iva/<int:precio>", methods=["GET"])
def calcular(precio : int)-> str:
    iva : float = precio * 0.19
    total : float = precio + iva
    return f"<h1>Calculadora de IVA</h1><p>Precio: ${precio} IVA: ${iva} Total: ${total}</p>"
@app.route("/api/convertir_temperatura/<float:celsius>", methods=["GET"])
def temperatura_celsius_a_fahrenheit(celsius : float) -> str:
    fahrenheit : float = (celsius * 9/5) + 32
    return f"<h1>Convertidor de Temperatura</h1><p>{celsius}°C son {fahrenheit}°F</p>"
if __name__ == "__main__":
    app.run(host = "192.168.1.24", port = 5000, debug=True)