# Creando la Clase "Gato"

class Gato():
    # Iniciando el Constructor
    def __init__(self, nombre, id, edad, energia, hambre, color, tamanio):
        self.nombre = str(nombre)
        self.id = int(id)
        self.edad = int(edad)
        self.energia = int(energia)
        self.hambre = int(hambre)
        self.color = str(color)
        self.tamanio = float(tamanio)
    
    # Creando el método para que el gato juegue
    def jugar(self):
        energia_perdida = 10
        hambre_aumentada = 5
        self.energia -= energia_perdida
        self.hambre += hambre_aumentada
        print(f"¡El gato {self.nombre} se puso a jugar!, a perdido {energia_perdida} pts. de energía y a aumentado en {hambre_aumentada} pts. su hambre.") 

    # Creando método para alimentar al gato 
    def alimentar(self):
        energia_recuperada = 20
        hambre_perdida = 15
        self.energia += energia_recuperada
        self.hambre -= hambre_perdida
        print(f"Haz alimentado a {self.nombre}, por lo que a recuperado {energia_recuperada} pts. de energía, y {hambre_perdida} pts")

    # Creando método mágico para mostrar información del gato
    def __str__(self):
        return f"| Nombre: {self.nombre} | Edad: {self.edad} | Energía: {self.energia} | Hambre {self.hambre} | Color {self.color} | Tamaño(kg): {self.tamanio:.2f} |\n"
        
    def __delattr__(self, gato):
        del gato
        print(f"El Gato {gato.nombre} ha salido del Café")

# Creando la clase "Espacio"
class Espacio():
    def __init__(self, nombre_espacio, capacidad):
        self.espacio = str(nombre_espacio)
        self.capacidad = int(capacidad)
        self.gatos = []

    def agregar_gato(self, gato):
        if gato in self.gatos:
            print(f'El gato {gato.nombre}, con ID: {gato.id} ya se encuentra en el espacio "{self.espacio}".')
        else:
            nuevo_gato = 1
            capacidad_nueva = self.capacidad - nuevo_gato # Creando variable para guardar la nueva capacidad
            self.capacidad = capacidad_nueva
            if capacidad_nueva < 0:
                print("La capacidad máxima de gatos se ha excedido, el gato no puede entrar.")
            elif capacidad_nueva >= 0:
                self.gatos.append(gato)
                print(f'El gato {gato.nombre} ha sido agregado al espacio "{self.espacio}"')

    def __str__(self):
        informacion = "\n==== Gatos ====\n" 
        for gato in self.gatos:
            informacion += str(gato)
        return informacion

# probando a crear una Clase "CafeGatos" para guardar los espacios
class CafeGatos():
    def __init__(self):
        self.espacios = []

    def agregar_espacio(self, espacio_nuevo):
        if espacio_nuevo in self.espacios:
            print(f"El espacio {espacio_nuevo.nombre_espacio} ya se encuentra en el Café")
        else:
            self.espacios.append(espacio_nuevo)
            print(f"El espacio {espacio_nuevo.nombre_espacio} ha sido agregado al Café")

    def __str__(self):
        return f"Espacios: {self.espacios}"

# Instanciando atributos del primer gato
gato1 = Gato("Halfonso", 143, 7, 30, 40, "Naranja", 3)
gato2 = Gato("Sky", 102, 2, 50, 30, "Gris", 1.5)

# Instanciando atributos del espacio
espacio1 = Espacio("Terraza", 2)

# Probando Métodos de la Clase "Gato"
gato1.jugar()
print(gato1)

# Probando Métodos de la Clase "Espacio"
espacio1.agregar_gato(gato1)
espacio1.agregar_gato(gato1)
espacio1.agregar_gato(gato2)
print(espacio1)

# Instanciando atributo a la Clase "Cafe"
cafe = CafeGatos()

# Probando Métodos de la Clase "CaféGatos" 
cafe.agregar_espacio(espacio1)

print(cafe)