from datetime import datetime 

# Creando la Clase "Reserva_Hostal"
class Reserva_Hostal():
    def __init__(self, nombre_cliente, fecha_entrada, fecha_salida, numero_habitacion):
        self.nombre_cliente = nombre_cliente
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.numero_habitacion = (numero_habitacion)

    def calcular_duracion_estadia(self):
        fecha_entrada = datetime.strftime(self.fecha_entrada, "%Y-%m-%d")
        fecha_salida = datetime.strftime(self.fecha_salida, "%Y-%m-%d")
        duracion = (fecha_salida - fecha_entrada)


cliente1 = Reserva_Hostal("Federico", "6-7-2025", "20-7-2025", 15 )