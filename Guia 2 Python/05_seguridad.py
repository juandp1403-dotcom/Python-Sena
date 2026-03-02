class SistemaSeguridad:
    def __init__(self, pin_acceso: int):
        self.usuario: str = 'admin'
        self.__pin_acceso: int = pin_acceso
        self.__alarmaactivada: bool = True
    def desactivar_alarma(self, pin: int) -> None:
        if pin == self.__pin_acceso:
            self.__alarmaactivada = False
            print('Alarma desactivada. Bienvenido admin.')
        else:
            print('Pin incorrecto. Intruso detectado.')

casa_central = SistemaSeguridad(1234)

casa_central.desactivar_alarma(4321)
casa_central.desactivar_alarma(1234)
exit()