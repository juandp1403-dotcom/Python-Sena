# Crear lista vacía
concesionario = []

# Bucle que se repite 3 veces
for i in range(3):
    print(f"\nRegistro del vehículo {i+1}")
    
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    precio = float(input("Precio: "))
    
    # Diccionario temporal
    carro = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }
    
    # Guardar diccionario en la lista
    concesionario.append(carro)

# Segundo bucle para mostrar informe
print("\n--- INFORME DE VEHÍCULOS ---")
for vehiculo in concesionario:
    print(f"Vehículo registrado: Marca {vehiculo['marca']}, "
          f"Modelo {vehiculo['modelo']}, "
          f"Precio: ${vehiculo['precio']}")
exit()