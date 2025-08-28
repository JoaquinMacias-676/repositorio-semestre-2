class Auto ():
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando")

    def girar(self):
        print(f"El {self.marca} {self.modelo} está girando")

    