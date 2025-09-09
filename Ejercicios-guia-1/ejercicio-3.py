# Creación de la Clase "Producto"
class Producto():
    # Constructor
    def __init__(self, nombre_producto, precio_u, stock, codigo_barra):
        self.nombre_producto = nombre_producto
        self.precio_u = int(precio_u)
        self.stock = int(stock)
        self.codigo_barra = str(codigo_barra)
        self.historial_stock = [stock]

    # Método para actualizar el stock
    def actualizar_stock(self, nuevo_stock):
        self.stock = int(nuevo_stock) # Cambiando al nuevo stock
        self.historial_stock.append(self.stock) # Agregando el stock nuevo al historial

    # Método para calcular el valor total del producto
    def valor_total(self):
        return self.precio_u * self.stock

    def __str__(self):
        return f"\nProducto: {self.nombre_producto} | Código de Barra: {self.codigo_barra} | Precio Unitario: ${self.precio_u} CLP | Cantidad: {self.stock} | Historial Stock: {self.historial_stock} | Valor Total: ${self.valor_total()} CLP\n"
    
class Inventario():
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.codigo_barra in  self.productos:
            print(f"El producto, con código de barra {producto.codigo_barra} ya se encuentra en el inventario")
        else:
            self.productos[producto.codigo_barra] = producto
            print(f"Agregando el producto con código de barra {producto.codigo_barra} al Inventario")

    def actualizar_stock_inv(self, codigo_barra, nuevo_stock ):
        if codigo_barra in self.productos:
            producto = self.productos[codigo_barra]
            antiguo_stock = producto.stock
            producto.actualizar_stock(nuevo_stock)
            print(f"El producto {producto.nombre_producto} con código de barra {producto} a actualizado su stock de {antiguo_stock} a {producto.stock}.")
        else:
            print(f"El producto ingresado no se encuentra en el inventario.")



producto1 = Producto("Cebolla", 500, 20, "78920000129")

producto1.actualizar_stock(10)
print(producto1)

inventario1 = Inventario()

inventario1.agregar_producto(producto1)
inventario1.agregar_producto(producto1)

inventario1.actualizar_stock_inv(78920000129, 40)