class Coche ():
    def __init__(self, marca, modelo, anio, color, gasolina):
        self.marca = str(marca)
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.gasolina = float(gasolina)

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando")

    def girar(self):
        print(f"El {self.marca} {self.modelo} está girando")
    
    def conducir(self):
        print("1")

coche1 = Coche("Ferrari", "F355", "1998", "rojo", "45")