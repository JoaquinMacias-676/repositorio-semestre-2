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
        stock_antiguo = self.stock # Variable para guardar el stock antiguo 
        self.historial_stock.append(self.stock) # Agregando el stock anterior al historial
        self.stock = int(nuevo_stock) # Cambiando al nuevo stock
        cambio_stock = stock_antiguo - self.stock # Variable para saber si hubo un aumento o decrecimiento del stock

    # Condicional para definir el aumento o decrecimiento del stock
        print(f"\nSe a cambiado la cantidad de {self.nombre_producto}, a pasado de {stock_antiguo} a {self.stock}.")
        if cambio_stock > 0:
            print(f"El stock de {self.nombre_producto} aumento")
        elif cambio_stock == 0:
            print(f"El stock de {self.nombre_producto} no a cambiado")
        else:
            print(f"El stock de {self.nombre_producto} a disminuido")
        print(f"Historial de stock: {self.historial_stock}\n")

    # Método para calcular el valor total del producto
    def valor_total(self):
        valor_total = self.precio_u * self.stock
        print(f"El valor total de todos los productos es de ${valor_total} CLP")

    def __str__(self):
        
producto1 = Producto("Cebolla", 500, 20, "7 89200 00129")

producto1.actualizar_stock(10)
producto1.valor_total()
