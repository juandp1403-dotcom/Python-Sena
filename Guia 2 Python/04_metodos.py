class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular: str = titular
        self.saldo: float = saldo_inicial
    def depositar(self, cantidad: float) -> None:
        self.saldo += cantidad
        print(f'Deposito exitoso. Nuevo saldo de {self.titular}: ${self.saldo}')
    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            print(f'Error {self.titular} no cuenta con ese dinero. Saldo actual: ${self.saldo}')
        else:
            self.saldo -= cantidad
            print(f'Retiro exitoso. Nuevo saldo: ${self.saldo}')

cuenta_ana = CuentaBancaria('Ana Lopez', 50000.0)
cuenta_ana.depositar(15000.0)
cuenta_ana.retirar(200000.0)
cuenta_ana.retirar(50000.0)
exit()