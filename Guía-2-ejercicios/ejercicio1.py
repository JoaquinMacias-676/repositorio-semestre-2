class Tarea:

    def __init__(self, id: int, titulo: str):
        self.id = id
        self.titulo = titulo
        self.hecha = False

class Agenda():

    __contador = 0

    def __init__(self):
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


        