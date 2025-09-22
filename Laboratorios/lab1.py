# Creando la Clase "Gato"

class Gato():
    # Iniciando el Constructor
    def __init__(self, nombre, id, edad, energia, hambre, color, tamanio, salud, estado_salud):
        self.nombre = str(nombre)
        self.__id = int(id)
        self.edad = int(edad)
        self.energia = int(energia)
        self.hambre = int(hambre)
        self.color = str(color)
        self.tamanio = float(tamanio)
        self.__salud = int(salud)
        self.estado_salud = str(estado_salud)
    
    # Creando el método para que el gato juegue
    def jugar(self):
        if self.energia < 20:
            print(f"{self.nombre} no tiene la energía suficiente para poder jugar, se encuentra por debajo de los 20 pts.")
        else:
            self.energia -= 10
            self.hambre += 5
            print(f"¡El gato {self.nombre} se puso a jugar!, a perdido energía y ahora tiene {self.energia} pts, además de aumentar su hambre y tener {self.hambre} pts.") 

    # Creando método para alimentar al gato 
    def alimentar(self):
        self.__salud +=5
        self.energia += 20
        self.hambre -= 15
        print(f"Haz alimentado a {self.nombre}, por lo que su energía ahora es de {self.energia} pts, su nivel de hambre es de {self.hambre} pts, y su salud es de {self.__salud} pts.")

    def __medicar(self):
        if self.__salud == 100:
            print(f"{self.nombre} ya se encuentra bien, no es necesario medicarlo.")
        else:
            self.__salud += 20
            print(f"{self.nombre} se a recuperado, ahora mismo se encuentra con {self.__salud} pts. de salud.")
            if self.__salud > 100:
                self.__salud = 100 

    # Creando método mágico para mostrar información del gato
    def __str__(self):
        return f"| Nombre: {self.nombre} | Edad: {self.edad} | Energía: {self.energia} | Hambre {self.hambre} | Color {self.color} | Tamaño(kg): {self.tamanio:.2f} |\n"
    
    def __del__(self):
        print(f"El Gato {self.nombre} ha salido del Café")

# Creando la clase "Espacio"
class Espacio():
    def __init__(self, nombre_espacio, capacidad):
        self.espacio = str(nombre_espacio)
        self.capacidad = int(capacidad)
        self.gatos = []

    def agregar_gato(self, gato):
        if len(self.gatos) < self.capacidad:
            if gato in self.gatos:
                print(f'El gato {gato.nombre} ya se encuentra en el espacio "{self.espacio}".')
            else:
                self.gatos.append(gato)
                print(f'El gato {gato.nombre} ha sido agregado al espacio "{self.espacio}"')
        else:
            print(f"No queda espacio para agregar a {gato.nombre}.")

    def __str__(self):
        informacion = "\n==== Gatos ====\n" 
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
gato1.jugar()
gato1.jugar()
gato1.jugar()
gato1.alimentar()
print(gato1)

# Probando Métodos de la Clase "Espacio"
espacio1.agregar_gato(gato1)
espacio1.agregar_gato(gato1)
espacio1.agregar_gato(gato2)
espacio1.agregar_gato(gato3)
print(espacio1)