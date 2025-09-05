# Creando primera Clase

class Cancion ():
    # Constructor
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = int(duracion_segundos)

    # Métodos

    # Convierte la duración a formato mm:ss (5:45)
    def milisegundos(self):
        m, s = divmod(max(self.duracion_segundos(), 0), 60)
        return f"{m}:{s}"

    def __str__(self):
        return f"{self.titulo} - {self.artista} - {self.duracion_segundos}"

# Creando segunda Clase

class Playlist ():
    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    # Agregar una canción a la Playlist
    def agregar(self, cancion):
        self.canciones.append(cancion)

    # Duración total de la Playlist    
    def duracion_total(self):
        return sum(c.duracion_segundos for c in self.canciones)

    def milisegundos_total(self):
        total = self.duracion_total()
        m, s = divmod(max(total, 0), 60)
        return f"{m}:{s}"
    
    def __len__(self):
        return len(self.canciones)
    
    # Combinando dos playlist
    def __add__(self, other):
        # Se crea una nueva variable que fusiona ambas playlist en una nueva 
        nueva = Playlist(f"{self.nombre} + {other.nombre}")

        # Guardando las canciones en la playlist combinados
        nueva.canciones = self.canciones + other.canciones
        return nueva
    
    def __str__(self):
        # Encabezado a Mostrar de la Playlist
        encabezado = f"Playlist: {self.nombre} | {len(self.canciones)}: Canciones | Total: {self.milisegundos_total}"

        # Lanzar mensaje si la lista esta vacía
        if not self.canciones:
            return encabezado, f"Lista Vacía"

        # Para la creación del formato de impresión de la Playlist
        lineas = [encabezado]

        # Creación de ciclo para mostrar el listado de canciones de la playlist combinado
        for i, c in enumerate(self.canciones):
            lineas.append(f"{i}: {c}")
            return "\n".join(lineas) # combina el salto de linea

playlist1 = Playlist("Pop", [])
cancion1 = Cancion("Hola", "aaa", 150)

cancion1.milisegundos()