carrito_compras = ['leche', 'pan', 'huevos']
print(f'El carrito de compras contiene: {carrito_compras}')
carrito_compras.append('cafe')
print(f'El carrito de compras actualizado con el cafe es: {carrito_compras}')
carrito_compras.remove('leche')
print(f'El carrito de compras después de eliminar la leche es: {carrito_compras}')
carrito_compras[1] = 'huevos campesinos'
print(f'El carrito de compras después de actualizar los huevos es: {carrito_compras}')
exit()