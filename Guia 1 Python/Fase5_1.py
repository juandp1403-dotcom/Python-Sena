dias_semana = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')
dia = int(input('Ingrese un día de la semana: '))
if dia == 1:
    print(f'El día de la semana es: {dias_semana[0]}')
elif dia == 2:
    print(f'El día de la semana es: {dias_semana[1]}')  
elif dia == 3:
    print(f'El día de la semana es: {dias_semana[2]}')
elif dia == 4:
    print(f'El día de la semana es: {dias_semana[3]}')
elif dia == 5:
    print(f'El día de la semana es: {dias_semana[4]}')  
elif dia == 6:
    print(f'El día de la semana es: {dias_semana[5]}')
elif dia == 7:
    print(f'El día de la semana es: {dias_semana[6]}') 
else:
    print('El número ingresado no corresponde a un día de la semana')
exit()