class Tarea:

    def __init__(self, id: int, titulo: str):
        self.id = id
        self.titulo = titulo
        self.hecha = False

class Agenda():

    __contador = 0

    def __init__(self, titulo):
        self.titulo = titulo
        self.__tareas = []

    def agregar(self, titulo: str):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        Agenda.__contador += 1
        tarea = Tarea(Agenda.__contador, titulo)
        self.__tareas.append(tarea)
        return tarea.id
    
    def marcar_hecha(self, id: int):
        for tarea in self.__tareas:
            if tarea.id == id:
                tarea.hecha = True
                return
        raise ValueError("Tarea no encontrada")
    
    def listar_pendientes(self):

        lista_pendientes = []

        for tareas in self.__tareas:
            if not tareas.hecha:
                lista_pendientes.append(tareas.titulo)
        
        if not lista_pendientes:
            raise ValueError("No hay tareas pendientes")
        
        return lista_pendientes
        
    def __len__(self):
        return len(self.__tareas)
    
    @classmethod
    def total_creadas(cls):
        return cls.__contador
    
# Intanciando
agenda1 = Agenda("Agenda 1")
agenda2 = Agenda("Agenda 2")

# Probando Métodos
agenda1.agregar("Hacer la cama")
agenda1.agregar("Cocinar")
agenda1.agregar("Lavar los platos")
agenda2.agregar("Estudiar")
agenda1.marcar_hecha(1)
print(f"Lista de tareas pendientes en {agenda1.titulo}: {agenda1.listar_pendientes()}")
print(f"Lista de tareas pendientes en {agenda2.titulo}: {agenda2.listar_pendientes()}")
print(f"Número total de tareas: {len(agenda1)}")
print(f"Total de Tareas Creadas: {Agenda.total_creadas()}")
