class Playlist():

    total_playlist = 0

    def __init__(self, usuario):
        self.usuario = usuario
        self.__canciones = []
        Playlist.total_playlist += 1

    def agregar_cancion(self, nombre: str):
        if not nombre:
            raise ValueError("La canción no puede estar vacía")
        if nombre in self.__canciones:
            raise ValueError("La canción no puede estar repetida en la Playlist")
        self.__canciones.append(nombre)

    def eliminar_cancion(self, nombre):
        if not nombre in self.__canciones:
            raise ValueError("La canción no se encuentra en la Playlist")
        self.__canciones.remove(nombre)

    def __len__(self):
        return len(self.__canciones)
    
    def __str__(self):
        return f"Playlist de {self.usuario}: {len(self)} canciones"
    
playlist1 = Playlist("Joaquin")
playlist1.agregar_cancion("Hola")
playlist1.agregar_cancion("A")
playlist1.agregar_cancion("Adios")
print(playlist1)
playlist1.eliminar_cancion("Hola")
print(playlist1)
