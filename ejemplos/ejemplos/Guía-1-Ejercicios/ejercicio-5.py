class Libro():
    def __init__(self, titulo, autor, anio_publicacion, cantidad_disponible ):
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.anio_publicacion = int(anio_publicacion)
        self.cantidad_disponible = int(cantidad_disponible)

class Biblioteca():
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, libro):
        if libro.titulo in self.libros:
            pregunta = str(input(f'El libro con titulo "{libro.titulo}" ya se encuentra en la biblioteca, \nquiere agregar más libro con el mismo título a la biblioteca? (Si o No): '))
            if pregunta.upper() == "SI":
               cantidad_antigua = libro.cantidad_disponible
               agregar_stock = int(input("¿Cúantos libros agregará?: "))
               libro.cantidad_disponible += agregar_stock
               print(f'La cantidad de libros disponibles de "{libro.titulo}" a pasado de {cantidad_antigua} a {libro.cantidad_disponible}')
            elif pregunta.upper() == "NO":
                print(f"Entendido.")
            else:
                print("La respuesta ingresada no coincide con ninguna de las opciones dadas.")
        else:
            self.libros[libro.titulo] = libro
            print(f'El libro con título "{libro.titulo}" se ha agregado a la Biblioteca')

libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 1989, 5)

biblioteca = Biblioteca()

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro1)