class Playlist():

    total_playlist = 0

    def __init__(self, usuario):
        self.usuario = usuario
        self.__canciones = []
        Playlist.total_playlist += 1

    def agregar_cancion(self, nombre: str):
        if not nombre:
            raise ValueError("La canción no puede estar vacía")
        for i in self.__canciones:
            if not nombre == i:
               self.__canciones.append(nombre)
            else:
                print("La canción no puede estar vacía")

    def eliminar_cancion(self, nombre):
        for i in self.__canciones: 
            if nombre == i:
                self.__canciones.remove(nombre)
            else:
                print("No se encontro la canción")

    def __len__(self):
        return len(self.__canciones)
    
    def __str__(self):
        return f"Playlist de {self.usuario}: {len(playlist1)} canciones"
    
playlist1 = Playlist("Joaquin")
playlist1.agregar_cancion("Hola")
playlist1.agregar_cancion("A")
playlist1.agregar_cancion("Adios")
print(playlist1)
playlist1.eliminar_cancion("Hola")
print(playlist1)
