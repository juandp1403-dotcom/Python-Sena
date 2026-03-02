print('--- FILTO DE SEGURIDAD ---')
edades_acceso = [15,22,17,30,14]
for edad in edades_acceso:
    if edad < 18:
        print(f'Persona de edad {edad} años: Accesso permitido')
    else:
        print(f'Persona de edad {edad} años: Acceso denegado')
exit()