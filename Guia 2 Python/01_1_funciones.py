def crear_perfil(nombre: str, rol: str) -> None:
    "Registra un perfil en el sistema."
    print(f"Registrando en base de datos {nombre} con permisos de {rol}")

crear_perfil("Carlos", "Admin")
crear_perfil("Ana", "Ventas")
exit()