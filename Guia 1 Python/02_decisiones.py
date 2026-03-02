edad_usuario = int(input('Por favor, ingresa tu edad: '))
print('Evaluando permisos del susario...')
if edad_usuario >= 18:
    print('Eres mayor de edad, puedes acceder al contenido.')
elif edad_usuario >= 13:
    print('Eres un adolescente, tienes acceso restringido pide ayuda a un tutor.')
else:
    print('Eres un niño, no tienes acceso al contenido.')
print('Gracias por usar nuestro sistema.')
exit()