# Se tomarán todas las medidas en cm
# Importando Librería math para usar pi y tan
import math

# Importando Librería random para utilizar números aleatorios en los objetos
import random as rd

# Creando Clases de Figuras
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = (self.radio ** 2) * math.pi
        return round(area, 2)

class Rectangulo:
    def __init__(self, base, alto):
        self.base = base
        self.alto = alto

    def calcular_area(self):
        area = self.base * self.alto
        return round(area, 2)
    
class Triangulo:
    def __init__(self, base, alto):
        self.base = base
        self.alto = alto

    def calcular_area(self):
        area = (self.base * self.alto) / 2
        return round(area, 2)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        area = self.lado ** 2
        return round(area, 2)

class Trapecio:
    def __init__(self, base_1, base_2, alto):
        self.base_1 = base_1
        self.base_2 = base_2
        self.alto = alto

    def calcular_area(self):
        area = ((self.base_1 + self.base_2) / 2) * self.alto
        return round(area, 2)

class Pentagono: # Pentagono Regular
    def __init__(self, lado):
        self.lado = lado
        self.perimetro = self.lado * 5
        self.apotema = self.lado / (2 * math.tan(36))

    def calcular_area(self):
        area = (self.perimetro * self.apotema) / 2
        return round(area, 2)
    
def mostrar_area(figura):
    print(f'La figura "{type(figura).__name__}" tiene un área de {figura.calcular_area()} cm²')

figuras = [
    Circulo(rd.randint(10, 20)),
    Rectangulo(rd.randint(30, 40), rd.randint(50, 70)),
    Triangulo(rd.randint(10, 20), rd.randint(10, 15)),
    Cuadrado(rd.randint(10, 40)),
    Trapecio(rd.randint(20, 30), rd.randint(20, 30), rd.randint(10, 15)),
    Pentagono(rd.randint(5, 20))
]

print("\n======== Áreas de Figuras Geométricas ========\n")
for figura in figuras:
    mostrar_area(figura)