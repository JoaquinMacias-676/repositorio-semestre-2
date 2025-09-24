# Creando la Clase "Gato"

class Gato():
    # Iniciando el Constructor
    def __init__(self, nombre, id, edad, energia, hambre, color, tamanio, salud, estado_salud):
        self.nombre = str(nombre)
        self.__id = int(id) # Encapsulando Id para no ser usado fuera de la Clase "Gato"
        self.edad = int(edad)
        self.energia = int(energia)
        self.hambre = int(hambre)
        self.color = str(color)
        self.tamanio = float(tamanio)
        self.__salud = int(salud) # Encapsulando la "salud" para no ser usado fuera de la Clase "Gato"
        self.__estado_salud = str(estado_salud) # Encapsulando el "estado de salud" para no ser usado fuera de la Clase "Gato"
        self.__historial = [estado_salud] # Encapsulando el "historial médico" para no ser usado fuera de la Clase "Gato"
    
    # Creando el método para que el gato juegue
    def jugar(self):
        if self.__salud == 0:
            return
       
        if self.energia < 20:
            print(f"{self.nombre} no tiene la energía suficiente para poder jugar, se encuentra por debajo de los 20 pts.")
        else:
            self.energia -= 10
            self.hambre += 5
            print(f"¡El gato {self.nombre} se puso a jugar!, a perdido energía y ahora tiene {self.energia} pts, además de aumentar su hambre y tener {self.hambre} pts.") 

    # Creando método para alimentar al gato 
    def alimentar(self):
        if self.__salud == 0:
            return
        
        self.energia += 20
        self.hambre -= 15
        print(f"Haz alimentado a {self.nombre}, por lo que su energía ahora es de {self.energia} pts, y su nivel de hambre es de {self.hambre} pts.")

    # Creando método para "atacar" al gato
    def perros(self):
        if self.__salud <= 0:
            return
        
        self.__salud -= 30
        print(f"El gato {self.nombre} salio afuera un momento y fue atacado por unos perros, por lo que sufrio heridas.")
        if self.__salud < 0:
            self.__salud = 0

    # Creando método privado para medicar al Gato
    def __medicar(self):
        if self.__salud == 0:
            return
        
        self.__salud += 20
        if self.__salud > 100:
            self.__salud = 100 

    # Creando método para realizar una revisión al gato y medicarlos si no se encuentra en su mejor estado
    def revision(self):
        if self.__salud == 0:
            print(f"{self.nombre} ya no se encuentra con vida, no se le puede realizar ninguna revisión.")
        else:
            print(f"Procediendo a realizar revisión médica a {self.nombre}.")
            if self.__salud == 100:
                print(f"{self.nombre} se encuentra en perfecto estado, no es necesario medicarlo.")
            else:
                self.__medicar()
                print(f"{self.nombre} no se encontraba al 100%, por lo que se le ha medicado, su salud ahora es de: {self.__salud} pts.")
                if self.__salud <= 40:
                    self.__historial.append("Enfermo")
                elif self.__salud <= 70:
                    self.__historial.append("En Observación")
                else:
                    self.__historial.append("Saludable")

    # Creando método para mostrar el historial médico del Gato
    def historial_medico(self):
        print(f"""
===== Historial Médico =====
ID: {self.__id}
Nombre: {self.nombre}
Estado Actual: {self.__estado_salud}
Historial de Estado(s): {self.__historial}
Veces que se medico al gato: {len(self.__historial) - 1}""")
        
    # Creando método mágico para mostrar información General del gato (excluyendo información médica)
    def __str__(self):
        return f"""
| Nombre: {self.nombre} |
|Edad: {self.edad} |
|Energía: {self.energia} |
|Hambre {self.hambre} |
|Color {self.color} |
|Tamaño(kg): {self.tamanio:.2f} |"""
    
    def __del__(self):
        if self.__salud > 0:
            print(f"El Gato {self.nombre} ha salido del Café.")
        else:
            print(f"El Gato {self.nombre} ha muerto :(.")

# Creando la clase "Espacio"
class Espacio():
    def __init__(self, nombre_espacio, capacidad):
        self.espacio = str(nombre_espacio)
        self.capacidad = int(capacidad)
        self.gatos = []

    # Creando método para agregar al Gato al Espacio
    def agregar_gato(self, gato):
        if len(self.gatos) < self.capacidad:
            if gato in self.gatos:
                print(f'El gato {gato.nombre} ya se encuentra en el espacio "{self.espacio}".')
            else:
                self.gatos.append(gato)
                print(f'El gato {gato.nombre} ha sido agregado al espacio "{self.espacio}".')
        else:
            print(f"No queda espacio para agregar a {gato.nombre}.")
    # Creando método que muestre la información general de todos los Gatos en el Espacio
    def __str__(self):
        informacion = "\n======= GATOS =======\n" 
        for gato in self.gatos:
            informacion += str(gato)
        return informacion

# Instanciando atributos del primer gato
gato1 = Gato("Halfonso", 143, 7, 30, 40, "Naranja", 3, 80, "Saludable")
gato2 = Gato("Sky", 102, 2, 50, 30, "Gris", 1.5, 50, "En observación")
gato3 = Gato("Goku", 78, 3, 60, 40, "Negro", 2, 20, "Enfermo")

# Instanciando atributos del espacio
espacio1 = Espacio("Terraza", 2)

# Probando Métodos de la Clase "Gato"
print("\n========== PROBANDO MÉTODOS CON EL PRIMER GATO ==========:\n")
gato1.jugar()
gato1.revision()
gato1.alimentar()
gato1.revision()
gato1.perros()
gato1.jugar()
gato1.revision()
gato1.historial_medico()
print(gato1)

print("\n========== PROBANDO MÉTODOS CON EL SEGUNDO GATO ==========\n")
gato2.jugar()
gato2.perros()
gato2.revision()
gato2.alimentar()
gato2.historial_medico
gato2.perros()
gato2.perros()
gato2.revision()
print(gato2)

# Probando Métodos de la Clase "Espacio"

print("\n========== PROBANDO MÉTODOS CON EL ESPACIO ==========\n")
espacio1.agregar_gato(gato1)
espacio1.agregar_gato(gato1)
espacio1.agregar_gato(gato2)
espacio1.agregar_gato(gato3)
print(espacio1)