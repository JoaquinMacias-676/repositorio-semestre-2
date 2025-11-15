import random as rd

class Vehiculo:

    def __init__(self, marca, modelo, velocidad, combustible):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.combustible = combustible

    def moverse(self):
        print("El vehículo se movio")

class Coche(Vehiculo):
    
    def __init__(self, marca, modelo, velocidad, combustible,):
        super().__init__(marca, modelo, velocidad, combustible)

class Lancha(Vehiculo):
    
    def __init__(self, velocidad, combustible):
        super().__init__(velocidad, combustible)

class VehiculoAnfibio(Vehiculo):
    
    def __init__(self, velocidad, combustible):
        super().__init__(velocidad, combustible)

class Hidroavion(Vehiculo):
    
    def __init__(self, velocidad, combustible, altura):
        super().__init__(velocidad, combustible)
    
vehiculos = [
    Coche("Toyota", "F12", (rd.randint(100, 200)), (rd.randint(40, 60))),
    Lancha("Toyota", "F12", (rd.randint(100, 200)), (rd.randint(40, 60))),
    VehiculoAnfibio("Toyota", "F12", (rd.randint(100, 200)), (rd.randint(40, 60))),
    Hidroavion("Toyota", "F12", (rd.randint(100, 200)), (rd.randint(40, 60)))
]
