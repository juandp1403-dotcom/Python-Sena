class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> bool:
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a cero.")

            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")

            self.stock -= cantidad
            print(f"Venta exitosa. Stock restante: {self.stock}")
            return True

        except ValueError as e:
            print(f"ADVERTENCIA: {e}")
            return False


class ProductoPerecedero(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento = dias_vencimiento

    def vender(self, cantidad: int) -> None:
        venta_exitosa = super().vender(cantidad)

        if venta_exitosa:
            print(f"Días para vencimiento: {self.dias_vencimiento}")

# Venta normal
producto1 = Producto("Laptop", 2500.0, 10)
producto1.vender(3)

# Intentar vender más del stock
producto2 = Producto("Mouse", 50.0, 5)
producto2.vender(10)

# Producto perecedero venta válida
producto3 = ProductoPerecedero("Leche", 4.5, 20, 7)
producto3.vender(5)

# Producto perecedero con cantidad inválida
producto4 = ProductoPerecedero("Yogurt", 3.0, 10, 5)
producto4.vender(0)