class Fraccion ():
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, other):
        nueva_fraccion = (self.numerador * other.denominador) + (other.numerador * self.denominador)
        nuevo_denominador = self.denominador * other.denominador 
        return Fraccion(nueva_fraccion, nuevo_denominador)
    
    def __mul__(self, other):
        return Fraccion(self.numerador * other.numerador, self.denominador * other.denominador)

    def __eq__(self, other):
        return self.numerador * other.denominador == other.numerador * self.denominador
     
fraccion_1 = Fraccion(2, 2)
fraccion_2 = Fraccion(5, 4)

suma = fraccion_1 + fraccion_2
producto = fraccion_1 * fraccion_2
comparacion = fraccion_1 == fraccion_2

print(f"La suma entre la fracción {fraccion_1} y {fraccion_2} es {suma}")
print(f"La multiplicación entre la fracción {fraccion_1} y {fraccion_2} da como producto {producto}")
print(f"¿La fracción {fraccion_1} y {fraccion_2} son iguales? {comparacion}")