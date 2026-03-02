def es_mayor_de_edad(edad: int) -> bool:
    "Determina si una persona es mayor de edad."
    return edad >= 18
edad_persona_1: int = 20
edad_persona_2: int = 15
if es_mayor_de_edad(edad_persona_1):
    print("La persona 1 es mayor de edad.")
else:
    print("La persona 1 es menor de edad.")
if es_mayor_de_edad(edad_persona_2):
    print("La persona 2 es mayor de edad.")
else:
    print("La persona 2 es menor de edad.")
exit()