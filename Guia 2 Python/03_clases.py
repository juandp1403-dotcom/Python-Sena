class servidor:
    def __init__(self, nombre:str, ip: str, ram_gp: int):
        self.nombre: str = nombre
        self.ip: str = ip
        self.ram_gp: int = ram_gp
        self.estado: str = 'apagado'
server_ventas= servidor('Ventas_01','192.198.1.10', 16)
server_bd= servidor('Database-Main', '10.0.0.5', 64)
print(f'El servidor {server_ventas.nombre} tiene {server_ventas.ram_gp}GB de RAM.')
print(f'El servidor {server_bd.nombre} tiene {server_bd.ram_gp}GB de RAM.')
exit()