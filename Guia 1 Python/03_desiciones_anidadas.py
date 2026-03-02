print('-- Diagnostico de red --')
hay_internet = input('¿Estan encendidas las luces del modem? (si/no): ')
if hay_internet == 'si':
    print('Paso 1: El equipo recibe energia.')
    luz_roja = input('¿Las luces del modem son rojas? (si/no): ')
    if luz_roja == 'si':
        print('Fallo detectado: Problema con la fibra oprica llame a soporte tecnico.')
    else:
        print('Todo normal su conexion esta perfecta.')
else:    print('Fallo critico: verifique que el equipo est ecnectado a la corriente.')
exit()