# Agregue profesión, para poder hacer un str y que quede mejor

class Trabajador:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion

    def tarea(self):
        return "Realizando tarea"
    
    def __str__(self):
        return f"|Nombre: {self.nombre} |Profesión: {self.profesion}|"
    
class Chef(Trabajador):
    def __init__(self, nombre, especialidad, profesion):
        Trabajador.__init__(self, nombre, profesion)
        self.especialidad = especialidad

    def tarea(self):
        return f"{self.nombre} esta cocinando su especialidad, que son: {self.especialidad}"
    
class Mesero(Trabajador):
    def __init__(self, nombre, seccion, profesion):
        Trabajador.__init__(self, nombre, profesion)
        self.seccion = seccion

    def tarea(self):
        return f"{self.nombre} esta atendiendo la sección {self.seccion}"
    
class AyudanteChefMesero(Chef, Mesero):
    def __init__(self, nombre, especialidad, seccion, profesion):
        Chef.__init__(self, nombre, especialidad, profesion)
        Mesero.__init__(self, nombre, seccion, profesion)

    def tarea(self):
        return Chef.tarea(self) + " y " + Mesero.tarea(self)

chef1 = Chef("José", "Fideos", "Chef")
mesero1 = Mesero("Juan", 2, "Mesero")
ayudante1 = AyudanteChefMesero("Diego", "Pizzas", 5, "Ayudante")

print("=========INICIO=========")
print("\nTrabajadores:\n")

print(chef1)
print(mesero1)
print(ayudante1)

print("\nLos trabajadores empezaron a hacer sus tareas:\n")
print(chef1.tarea())
print(mesero1.tarea())
print(ayudante1.tarea())

print("\n=========FIN=========")