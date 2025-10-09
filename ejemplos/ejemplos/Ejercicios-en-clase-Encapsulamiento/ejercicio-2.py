# SISTEMA DE GESTIÓN DE LIBRERÍA CHILOÉ

class Libreria():
    def __init__(self, nombre):
        self.__nombre = str(nombre)
        self.__catalogo = {}

    def agregar_libro(self, libro):
        if libro in self.__catalogo:
            print("El libro ya se encuentra en el catalogo")
class Libro():
    def __init__(self, titulo, precio):
        self.titulo = str(titulo)
        self.precio = int(precio)
        assert self.precio <= 0, print("ERROR: El libro no puede tener un precio menor o igual a 0") 
        
class Cliente():
    def __init__(self, id, nombre, compras, ):
        self.id = id
        self.nombre = nombre
        self.compras = []

class Carrito():
    def __init__(self):
        self.libros_agregados = 0

    def pagar(self):
        print("a")
        
# Agregar la cantidad total a pagar







libro1 = Libro("HOLA", 1500)
Libreria = Libreria("Librería Gabriela Mistral")