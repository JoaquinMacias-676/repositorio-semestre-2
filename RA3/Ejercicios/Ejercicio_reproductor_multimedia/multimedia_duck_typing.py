from multimedia_LSP import Audio, Video, Imagen

class BaseDeDatos:
    def __init__(self):
        self.datos = {}

    def obtener_peso(self):
        return 1500
    
def compresor_universal(objeto):
    try:
        peso = objeto.obtener_peso()
        print(f"Comprimiendo {type(objeto).__name__}... Tamaño: {peso} MB")
    except AttributeError:
        print(f"Error: El objeto {type(objeto).__name__} no es comprimible")

cancion = Audio("Bohemian_Rhapsody.mp3", 15)
foto = Imagen("Diagrama_UML.jpg", 5)

mi_bd = BaseDeDatos()

texto = "Hola Mundo"

cosas_para_comprimir = [cancion, foto, mi_bd, texto]

print("--- INICIANDO COMPRESIÓN ---")
for cosa in cosas_para_comprimir:
    compresor_universal(cosa)