class Vehiculo():
    def __init__(self, marca, modelo, anio):
        self.__marca = str(marca)
        self.__modelo = str(modelo)
        self.__anio = int(anio)
        self.__disponibilidad = True
        assert self.__anio >= 1500, print("ERROR: El año del vehículo es demasiado bajo")

    def marcar_vendido(self):
        self.__disponibilidad = "No disponible"

    def __str__(self):
        return f"Marca: {self.__marca} Modelo: {self.__modelo} Año: {self.__anio} Disponibilidad: {self.__disponibilidad}"
    
class Concecionario():
    def __init__(self):
        self.lista_vehiculos = []

    def agregar_vehiculo(self, vehiculo_nuevo):
        if vehiculo_nuevo in self.lista_vehiculos:
            print(f"El vehículo ya se encuentra dentro del Concecionario.")
        else:
            self.lista_vehiculos.append(vehiculo_nuevo)
            print(f"El vehículo a sido agregado al Concecionario")

    def mostrar_vehiculos(self):
        if len(self.lista_vehiculos) == 0:
            print("No hay vehículos en el Concecionario")
        else:
            print(f"========= VEHÍCULOS =========")
            for vehiculo in self.lista_vehiculos:
                print(f"{vehiculo.__marca} {vehiculo.__modelo} {vehiculo.__anio}")

auto1 = Vehiculo("Toyota", "F10", 1980)

auto1.marcar_vendido
print(auto1)

concencionario = Concecionario()

concencionario.agregar_vehiculo(auto1)
concencionario.mostrar_vehiculos()