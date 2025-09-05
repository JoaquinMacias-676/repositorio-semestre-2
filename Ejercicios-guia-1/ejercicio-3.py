# Creación de la Clase "Producto"
class Producto():
    # Constructor
    def __init__(self, nombre_producto, precio_u, stock, codigo_barra):
        self.nombre_producto = nombre_producto
        self.precio_u = int(precio_u)
        self.stock = int(stock)
        self.codigo_barra = str(codigo_barra)
        self.historial_stock = []

    # Método para actualizar el stock
    def actualizar_stock(self, nuevo_stock):
        self.historial_stock.append(self.stock) # Agregando el stock anterior al historial
        self.stock = int(nuevo_stock) # Cambiando al nuevo stock

    # Método para calcular el valor total del producto
    def valor_total(self):
        return self.precio_u * self.stock

    def __str__(self):
        return f"\nProducto: {self.nombre_producto} | Código de Barra: {self.codigo_barra} | Precio Unitario: ${self.precio_u} CLP | Cantidad: {self.stock} | Historial Stock: {self.historial_stock} | Valor Total: ${self.valor_total()} CLP\n"
    
producto1 = Producto("Cebolla", 500, 20, "7 89200 00129")

producto1.actualizar_stock(10)
print(producto1)