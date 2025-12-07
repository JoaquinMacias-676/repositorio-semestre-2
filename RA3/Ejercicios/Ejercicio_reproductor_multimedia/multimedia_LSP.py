class ArchivoMultimedia:
    def __init__(self, nombre, tamano_mb):
        self.nombre = nombre
        self.tamano_mb = tamano_mb

    def obtener_peso(self):
        return self.tamano_mb
    
class Reproducible(ArchivoMultimedia):
    def reproducir(self):
        pass

class Audio(Reproducible):
    def reproducir(self):
        print(f"Reproduciendo audio: {self.nombre}")

class Video(Reproducible):
    def reproducir(self):
        print(f"Reproduciendo vídeo: {self.nombre}")

class Imagen(ArchivoMultimedia):
    def mostrar(self):
        print(f"Mostrando imagen en pantalla: {self.nombre}")

def reproductor_seguro(medio: Reproducible):
    medio.reproducir()

audio = Audio("canción.mp3", 5)
video = Video("vídeo.mp4", 200)
imagen = Imagen("foto.jpg", 2)

lista_reproducible = [audio, video]

for item in lista_reproducible:
    reproductor_seguro(item)