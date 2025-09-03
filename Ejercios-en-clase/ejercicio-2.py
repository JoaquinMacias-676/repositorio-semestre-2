km_recorrer = float(input("Ingrese la cantidad de kilometros que desea recorrer: "))

class Coche ():
    def __init__(self, marca, modelo, anio, color, gasolina, kilometros_recorridos):
        self.marca = str(marca)
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.gasolina = float(gasolina)
        self.kilometros_recorridos = float(kilometros_recorridos)

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando")

    def girar(self):
        print(f"El {self.marca} {self.modelo} está girando")
    
    def conducir(self):
        gasolina_resta = km_recorrer / 10
        self.gasolina -= gasolina_resta
        if self.gasolina < 0:
            print(f"El coche {self.marca} {self.modelo} no dispone de la gasolina suficiente para seguir conduciendo, a logrado recorrer km de {km_recorrer} km solicitados.")
        elif self.gasolina == 0:
            print(f"El coche {self.marca} {self.modelo} se ha quedado sin gasolina, pero a logrado recorrer los {km_recorrer} km solicitados.")
        else:
            print(f"El coche {self.marca} {self.modelo} a recorrido {km_recorrer} km, le queda {self.gasolina} L de gasolina")

    def cargar_gasolina(self):
        gasolina_a_cargar = float(input("Ingrese la cantidad de gasolina que desea agregar: "))
        self.gasolina += gasolina_a_cargar

coche1 = Coche("Ferrari", "F355", "1998", "rojo", 10, 0)

coche1.conducir()

print("¿Desea recargar gasolina?")
peticion = int(input("Si es así, escriba 1, si no escriba 2: "))
if peticion == 1:
    coche1.cargar_gasolina()
elif peticion == 2:
    print("Tenga un buen día")
else:
    print("Opción incorrecta")