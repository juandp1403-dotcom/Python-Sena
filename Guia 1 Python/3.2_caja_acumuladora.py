total_ahorrado = 0
for mes in range(1, 4):
    consignacion = float(input(f'Ingrese el monto ahorrado en el mes {mes}: '))
    total_ahorrado += consignacion
print(f'Ahorro completado, el total de sus ahorros es: ${total_ahorrado}')
exit()