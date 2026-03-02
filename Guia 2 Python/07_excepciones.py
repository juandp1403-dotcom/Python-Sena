class CajeroAutomatico:
    def __init__(self):
        self.saldo: float = 10000.0
    def solicitar_retiro(self) -> None:
        print('--- Bienvenido al cajero ---')

        try:
            monto_str: str = input('Ingrese el monto a retirar (Solo numeros): ')
            monto: float = float(monto_str)
            if monto <= 0:
                raise ValueError('El monto debe ser mayor a cero.')
            self.saldo -= monto
            print(f'Retiro exitoso. Saldo restante: ${self.saldo}')
        except ValueError as e:
            print(f'ERROR DE FORMATO: Usted ingreso caracteres invalidos. {(e)}')
        except Exception as e:
            print(f'ERROR CRITICO DESCONOCIDO: Contacte a soporte {(e)}')
        finally:
            print('Expulsando la tarjeta... Gracias por usar el cajero. Vuelva pronto.')

mi_cajero = CajeroAutomatico()
mi_cajero.solicitar_retiro()
exit()