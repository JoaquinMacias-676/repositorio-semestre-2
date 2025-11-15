# Ejercicio Sistema de Gestión de pagos

class MetodoDePago:
    def __init__(self, numero, numeroatras, estado):
        self.estado = False

class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"|Producto: {self.nombre}|Precio Unitario: {self.precio}|Cantidad Disponible: {self.cantidad}|"
    
class Productos:
    def __init__(self):
        self.listaproductos = []
 
producto1 = Producto("a", 20, 2)

print(producto1)
print("Que desea comprar?")