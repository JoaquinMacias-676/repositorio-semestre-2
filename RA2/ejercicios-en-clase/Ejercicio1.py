import random as rd

ronda = 1

class Vehiculo:
    def __init__(self, modelo, velocidad):
        self.modelo = modelo
        self.velocidad = velocidad
        self.recorrido = 0

    def rodar(self):
        pass

    def navegar(self):
        pass

    def volar(self):
        pass

class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad,):
        super().__init__(modelo, velocidad)
        self.marca = marca

    def rodar(self):
        print(f"El Auto {self.marca} {self.modelo} esta rodando. (a recorrido {self.recorrido})")
        self.recorrido += self.velocidad

class Lancha(Vehiculo):
    def __init__(self, modelo, velocidad):
        super().__init__(modelo, velocidad)

    def navegar(self):
        print(f"La Lancha {self.modelo} esta navegando (a recorrido {self.recorrido})")
        self.recorrido += self.velocidad

class VehiculoAnfibio(Vehiculo):
    def __init__(self, modelo, velocidad):
        super().__init__(modelo, velocidad)
        
    def rodar(self):
        print(f"El VehículoAnfibio {self.modelo} esta rodando (a recorrido {self.recorrido})")
        self.recorrido += self.velocidad

    def navegar(self):
        print(f"El VehículoAnfibio {self.modelo} esta navegando (a recorrido {self.recorrido})")
        self.recorrido += self.velocidad

class Hidroavion(Vehiculo):
    
    def __init__(self, modelo, velocidad, altura):
        super().__init__(modelo, velocidad)
        self.altura = altura
    
    def navegar(self):
        print(f"El Hidroavión esta navegando (a recorrido {self.recorrido})")
        self.recorrido += self.velocidad
    def volar(self):
        print(f"El Hidroavión esta volando (a recorrido {self.recorrido})")
        self.recorrido += self.velocidad

vehiculos = [
    Coche("Toyota", "F12", (rd.randint(100, 200))),
    Lancha("T10", (rd.randint(100, 200))),
    VehiculoAnfibio("T201", (rd.randint(100, 200))),
    Hidroavion("A20", int(rd.randint(100, 200)), int(rd.randint(100, 300)))
]

for vehiculo in vehiculos:
    while vehiculo.recorrido <= 1000:
        for vehiculo in vehiculos:
            print(f"Ronda {ronda}")
            vehiculo.rodar()
            vehiculo.navegar()
            vehiculo.volar()
            ronda +=1
            print("")

print("Fin de la carrera")
for vehiculo in vehiculos:
    print(f"El vehículo {vehiculo.modelo} recorrio: {vehiculo.recorrido}km")