def calcular_area_rectangulo (base: float, altura: float) -> float:
    "Calcula y retorna el área de un rectángulo."
    area: float = base * altura
    return area
area_rectangulo_1: float = calcular_area_rectangulo(5.0, 3.0)
area_rectangulo_2: float = calcular_area_rectangulo(10.0, 4.0)
print(f"Área del rectángulo 1: {area_rectangulo_1}")
print(f"Área del rectángulo 2: {area_rectangulo_2}")
exit()