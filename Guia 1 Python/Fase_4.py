mis_amigos = []
for i in range(3):
    nombre = input(f'Ingrese el nombre de su amigo {i + 1}: ')
    mis_amigos.append(nombre)
print('Saludos personalizados:')
for amigo in mis_amigos:
    print(f'Hola {amigo}, ¡qué gusto saludarte!')
colores = ['Rojo', 'Azul', 'Verde']

color_no_gusta = input('Escribe un color que no te guste (Rojo, Azul o Verde): ')

if color_no_gusta in colores:
    colores.remove(color_no_gusta)
    print('Color eliminado correctamente.')
else:
    print('Ese color no está en la lista.')

print('Lista final de colores:', colores)
exit()