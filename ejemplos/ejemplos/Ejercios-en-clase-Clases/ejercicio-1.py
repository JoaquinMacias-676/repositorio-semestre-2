print("\nIngrese tres notas para saber si a aprobado la asignatura o no\n")

nota1 = float(input("Ingrese la primera nota:"))
nota2 = float(input("Ingrese la segunda nota:"))
nota3 = float(input("Ingrese la tercera nota:"))

class Persona ():
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)

    def hablar(self):
        print(f"{self.nombre} esta hablando")
        
    def caminar(self):
        print(f"{self.nombre} esta caminando")

    def calcular_imc(self):
        imc = self.peso / self.altura ** 2
        print(f"El índice de Masa corporal de {self.nombre} {self.apellido} es de {round(imc, 2)} ")
        if imc < 18.5:
            print(f"Entra en la categoría de bajo peso.")
        elif imc > 18.5 or imc < 24.9:
            print(f"Entra en la categoría de peso normal.")
        elif imc >= 25 or imc < 29.9:
            print(f"Entra en la categoría de sobrepeso.")
        else:
            print(f"Entra en la categoría de obesidad") 

    def promedio_asignatura(self):
        notas = [nota1, nota2, nota3]
        promedio = sum(notas)/len(notas)
        print(f"El promedio resultante es de {round(promedio, 2)}")
        if promedio < 4.0:
            print("Tuvo un promedio menor a lo exigido, no aprobo la asignatura.")
        else:
            print("Usted tuvo un promedio mayor a lo exigido, esta aprobado.")
    
persona1 = Persona("Cristina", "Torres", 23, 1.60, 58)
persona2 = Persona("Benjamin", "Gomez", 20, 1.75, 72)

persona1.calcular_imc()
persona1.promedio_asignatura()