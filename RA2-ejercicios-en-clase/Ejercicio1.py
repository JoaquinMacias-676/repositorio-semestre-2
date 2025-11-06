# Creando Clase Animal
class Animal:
    def __init__(self, nombre, edad, peso, genero):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.genero = genero

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

    def mostrar_ficha(self):
        print(f"El nombre del animal es:{self.nombre}, su edad es:{self.edad}, su peso es de:{self.peso} Kg, y su género es:{self.genero}")

# Clase Perro que herada la Clase Animal
class Perro(Animal):
    def __init__(self, nombre, edad, peso, genero, raza):
        super().__init__(nombre, edad, peso, genero)
        self.raza = raza
        
    def ladrar(self):
        print(f"{self.nombre} está ladrando")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"El nombre del animal es: {self.nombre}, su edad es: {self.edad}, su peso es de: {self.peso} Kg, su género es: {self.genero}, y su raza: {self.raza}")

# Clase Gato que herada la Clase Animal
class Gato(Animal):
    def __init__(self, nombre, edad, peso, genero, color_pelaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_pelaje
        
    def maullar(self):
        print(f"{self.nombre} esta amaullando")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"El nombre del animal es: {self.nombre}, su edad es: {self.edad}, su peso es de: {self.peso} Kg, su género es: {self.genero}, y su color de pelaje: {self.color_pelaje}")


# Clase Pajaro que herada la Clase Animal
class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, genero, color_plumaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_plumaje = color_plumaje

    def volar(self):
        print(f"{self.nombre} está volando alto")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"El nombre del animal es: {self.nombre}, su edad es: {self.edad}, su peso es de: {self.peso} Kg, su género es: {self.genero}, y su color de plumaje: {self.color_plumaje}")

# Creando Objetos
perro1 = Perro("Jack", 12, 100, "marciana", "doberman")

gato1 = Gato("Wiskas", 90, 80, "extraterrestre", "negro")
0
pajaro1 = Pajaro("Sparrow", 2, 4, "loro", "verde")

# Métodos de Perro

print("\nPerro:\n")
perro1.mostrar_ficha()

perro1.comer()

perro1.dormir()

perro1.ladrar()

# Métodos de Gato

print("\nGato:\n")

gato1.mostrar_ficha()

gato1.comer()

gato1.dormir()

gato1.maullar()

# Métodos de Pájaro

print("\nPájaro:\n")

pajaro1.mostrar_ficha()

pajaro1.comer()

pajaro1.dormir()

pajaro1.volar()
