class MascotaVirtual:
    def __init__(self, nombre: str, energia_inicial: int = 10):
        self.nombre: str = nombre
        self.energia: int = energia_inicial
        pass
    def jugar(self) -> None:
        if self.energia > 0:
            self.energia -= 3
            print(f'{self.nombre} está jugando. Energía restante: {self.energia}')
        else:
            print(f'{self.nombre} está demasiado cansada para jugar.')
    def dormir(self) -> None:
        self.energia += 5
        print(f'{self.nombre} está durmiendo. Energía actual: {self.energia}')

mi_mascota = MascotaVirtual('Pupo')
mi_mascota.jugar()
mi_mascota.dormir()
exit()
