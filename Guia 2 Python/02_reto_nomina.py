def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:
    salario_neto= salario_base - (salario_base * 0.08)
    salario_neto += bonificacion
    return salario_neto
# Datos de prueba
salario = 2000000
bono = 200000

# Llamar la función
resultado = calcular_salario_neto(salario, bono)

# Mostrar resultado
print(f"El salario neto es: ${resultado}")
exit()