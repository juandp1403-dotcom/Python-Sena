acumuladora = 0
for compra in range(1, 6):
    monto = float(input(f'Ingrese el monto de la compra {compra}: '))
    acumuladora += monto
print(f'El total acumulado de las compras es: ${acumuladora}')
exit()