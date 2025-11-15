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
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso}")
        print(f"Género: {self.genero}")

# Clase Perro que herada la Clase Animal
class Perro(Animal):
    def __init__(self, nombre, edad, peso, genero, raza):
        super().__init__(nombre, edad, peso, genero)
        self.raza = raza
        
    def ladrar(self):
        print(f"{self.nombre} está ladrando")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"Raza: {self.raza}")

# Clase Gato que herada la Clase Animal
class Gato(Animal):
    def __init__(self, nombre, edad, peso, genero, color_pelaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_pelaje
        
    def maullar(self):
        print(f"{self.nombre} esta amaullando")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"Color Pelaje: {self.color_pelaje}")


# Clase Pajaro que herada la Clase Animal
class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, genero, color_plumaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_plumaje = color_plumaje

    def volar(self):
        print(f"{self.nombre} está volando alto")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"Color de plumaje: {self.color_plumaje}")

# Creando Objetos

animales= [
    Perro("Jack", 12, 100, "Marciana", "Doberman"),
    Gato("Wiskas", 90, 80, "Extraterrestre", "Negro"),
    Pajaro("Sparrow", 2, 4, "Loro", "Verde")
]

# Bucle para probar métodos
for animal in animales:
    print(f"==== Ficha de {animal.nombre}")
    animal.mostrar_ficha()
    animal.comer()
    animal.dormir()
    
# Métodos Únicos

