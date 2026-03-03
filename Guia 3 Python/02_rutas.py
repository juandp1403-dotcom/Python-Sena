from flask import Flask
app = Flask(__name__)
@app.route("/api/saludar/<string:nombre>", methods=["GET"])
def saludar(nombre : str)-> str:
    return f"Hola {nombre}!Tu solicitud fue enrutada correctamente."
@app.route("/api/calcular_iva/<int:precio>", methods=["GET"])
def calcular(precio : int)-> str:
    iva : float = precio * 0.19
    total : float = precio + iva
    return f"Precio: ${precio} IVA: ${iva} Total: ${total}"
@app.route("/api/convertir_temperatura/<float:celsius>", methods=["GET"])
def temperatura_celsius_a_fahrenheit(celsius : float) -> str:
    fahrenheit : float = (celsius * 9/5) + 32
    return f"{celsius}°C son {fahrenheit}°F"
if __name__ == "__main__":
    app.run(debug=True)