# Creando Clase Principal
class Contenido:
    def __init__(self, titulo: str, anio: int):
        self.titulo = titulo
        self.anio = anio

    def mostrar_detalle(self):
        print(f"|Título: {self.titulo}|Año: {self.anio}|")

# Creando Clases de Tipo
class Reproducible(Contenido):
    def __init__(self, titulo: str, anio: int):
        Contenido.__init__(self, titulo, anio)

    def reproducir():
        pass

class Calificable(Contenido):
    def __init__(self, titulo: str, anio: int):
        Contenido.__init__(self, titulo, anio)
        self.rating = float(0.0)

    def calificar(self, puntuacion):
        self.rating = puntuacion
        print(f"Calificando, la calificación es: {self.rating}|")

# Creando Subclases
class Pelicula(Reproducible):
    def __init__(self, titulo: str, anio: int, duracion_minutos: int):
        Reproducible.__init__(self, titulo, anio)
        self.duracion_minutos = duracion_minutos

    def reproducir(self):
        return(f'Reproduciendo Película "{self.titulo}"')

class Documental(Contenido):
    def __init__(self, titulo: str, anio: int, tema: str):
        Contenido.__init__(self, titulo, anio)
        self.tema = tema

class Miniserie(Reproducible, Calificable):
    def __init__(self, titulo: str, anio: int, num_episodios: int):
        Reproducible.__init__(self, titulo, anio)
        self.num_episodios = num_episodios

    def reproducir(self):
        print(f'Reproduciendo Miniserie: "{self.titulo}"')

# Intentando crear función para usar reproducir()
def lista_de_reproduccion(lista_contenidos: list):
    for contenido in lista_contenidos:
        if type(contenido).__base__ == Reproducible:
            contenido.reproducir()

# Creando Objetos
pelicula = Pelicula("Cómo entrenar a tu dragón 2", 2014, 120)
documental = Documental("La vida", 1993, "Seres vivos")
miniserie = Miniserie("Breaking Bad", 2007, 13)

# Guardando Objetos en una lista
lista_mixta = [pelicula, documental, miniserie]

# Imprimiendo
print("====Probando a usar función de reproducir en objetos====\n")
lista_de_reproduccion(lista_mixta)

print("\n====Probando los 3 Métodos en Miniserie====\n")
miniserie.mostrar_detalle()
miniserie.reproducir()
miniserie.calificar(8)