class vehiculo:
    def __init__(self, marca: str, modelo: str, año: int):
        self.marca: str = marca
        self.modelo: str = modelo
        self.año: int = año
        self.estado: str = 'Disponible'
carro1 = vehiculo('Toyota', 'Corolla', 2020)
carro2 = vehiculo('Honda', 'Civic', 2019)
carro3 = vehiculo('Ford', 'Focus', 2018)
print(f'El carro {carro1.marca} {carro1.modelo} del año {carro1.año} está {carro1.estado}.')
print(f'El carro {carro2.marca} {carro2.modelo} del año {carro2.año} está {carro2.estado}.')
print(f'El carro {carro3.marca} {carro3.modelo} del año {carro3.año} está {carro3.estado}.')
exit()