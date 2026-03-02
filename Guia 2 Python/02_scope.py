impuesto_nacional: float = 0.19

def calcular_descuento(precio: float) -> float:
    descuento_total: float = precio * 0.10
    precio_con_impuesto: float = precio + (precio * impuesto_nacional)
    return precio_con_impuesto - descuento_total
resultado: float = calcular_descuento(1000.0)
print(f"El resultado del descuento es: {resultado}")
exit()