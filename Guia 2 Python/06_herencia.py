class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre: str = nombre
        self.salario: float = salario
    def trabajar(self) -> None:
        print(f'{self.nombre} está trabajando.')

class Desarrollador(Empleado):
    def programar(self) -> None:
        print(f'{self.nombre} está programando en python.')

class Gerente(Empleado):
    def dirigir(self) -> None:
        print(f'{self.nombre} está en una reunion estrategica.')

dev = Desarrollador('Carlos', 3000.0)
jefe = Gerente('Ana', 6000.0)
dev.trabajar()
dev.programar()
jefe.trabajar()
exit()