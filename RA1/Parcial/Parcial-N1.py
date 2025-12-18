class Jugador():
    jugadores_creados = 0
    POSICIONES_VALIDAS = {"DEL", "VOL", "DEF", "ARQ"}

    def __init__(self, nombre: str, edad: int, posicion: str, club: str, energia: int):
        if not self.posicion_valida(posicion):
            raise ValueError("El jugador no tiene una posición válida.")
        if not club:
            raise ValueError("El nombre del club no puede estar vacío.")
        self.__nombre = nombre
        self.__edad = edad
        self.__posicion = posicion
        self.club = club
        self.energia = energia
        self.__goles = 0
        Jugador.jugadores_creados += 1
        assert self.__edad >= 15, print("Edad no válida")
        assert 0 <= self.energia <= 100, print("Energía no válida")
        assert self.goles >= 0, print("El jugador debe de tener más de 0 goles")

    # Método para mostrar los Jugadores creados
    @classmethod
    def creados(cls):
        return cls.jugadores_creados
    
    # Método para mostrar si la posición del Jugador es válida
    @staticmethod
    def posicion_valida(posicion):
        return posicion in Jugador.POSICIONES_VALIDAS
            
    # Método para mostrar el nombre del Jugador
    @property
    def nombre(self):
        return self.__nombre
    
    # Método para mostrar la edad del Jugador
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad <= 15:
            raise ValueError("La edad nueva no es válida")
        self.__edad = nueva_edad

    # Método para mostrar la posición del Jugador
    @property
    def posicion(self):
        return self.__posicion
    
    # Método para mostrar los goles del Jugador
    @property
    def goles(self):
        return self.__goles
    
    # Método para entrenar al Jugador
    def entrenar(self, minutos):
        if minutos <= 0:
            raise ValueError("El jugador no puede entrenar 0 minutos o menos.")
        self.energia -= minutos
        assert 0 <= self.energia <= 100, print("Energía no válida")

    # Método para anotar gol
    def anotar_gol(self):
        self.__goles += 1
        assert self.__goles >= 0, print("Los goles no pueden ser menores o iguales a 0")
        return print("Anoto un gol.")

    # Método para mostrar información del jugador
    def __str__(self):
        return f"|Nombre Jugador: {self.nombre}|Club: {self.club}|Posición: {self.posicion}|Energía: {self.energia}|Goles: {self.goles}"


jugador1 = Jugador("Joaquin", 19, "DEL", "Deportes Castro", 90)
jugador2 = Jugador("Felipe", 36, "ARQ", "Deportes Castro", 30)
jugador1.club = ""
jugador1.energia = 70
jugador1.edad = 17
jugador1.anotar_gol()
jugador1.entrenar(20)
print(f"Nombre del jugador 1: {jugador1.nombre}\n")
print(f"Jugadores Creados: {Jugador.creados()}\n")
print(jugador1)