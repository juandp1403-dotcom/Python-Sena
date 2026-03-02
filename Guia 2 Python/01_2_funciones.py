def calcular_iva(precio_base: float) -> float:
    "Calcula y retorna el precio base con el IVA incluido."
    iva: float = precio_base * 0.19
    precio_final: float = precio_base + iva
    return precio_final

factura_1: float = calcular_iva(10000.0)
factura_2: float = calcular_iva(50000.0)

print(f"Total a pagar factura 1: {factura_1}")
print(f"Total a pagar factura 2: {factura_2}")
exit()    