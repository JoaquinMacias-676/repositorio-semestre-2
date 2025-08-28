
# Las clases van en MAYÚSCULAS, debido a que las funciones se usan con MINÚSCULAS

"""class Animal ():
    nombre = vaca
    especie = mamifero"""

# Para mantener el código y depurarlo, es mejor hacerlo como la forma de abajo, la de arriba es "peor"

class Animal ():
    # Constructor de la clase Animal
    # Atributos de la clase Animal (que se comparrtiran entre otros animales)
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

# self permite acceder a lo anterior
    def hacer_sonido (self):
        print(f"{self.nombre} está hablando")

    def correr (self):
        print(f"{self.nombre} está durmiendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# Creando un objeto de la clase Animal (le agrega un valor al nombre y la especie anterior)
gatito = Animal("Michi", "Gato") # Se debe de agregar a todos los atributos su debido parámetro, si se olvida alguno ocurrirá un error
perrito = Animal("Ali", "Perro")
loro = Animal("Chimuelo (Loro)", "Ave")

print(f"El nombre del animal es: {gatito.nombre}")
print(f"La especie del animal es de un: {gatito.especie}\n")

print(f"El nombre del animal es: {perrito.nombre}")
print(f"La especie del animal es de un: {perrito.especie}\n")

print(f"El nombre del animal es: {loro.nombre}")
print(f"La especie del animal es de un: {loro.especie}\n")

gatito.correr()
perrito.hacer_sonido()
loro.dormir()

#Probando