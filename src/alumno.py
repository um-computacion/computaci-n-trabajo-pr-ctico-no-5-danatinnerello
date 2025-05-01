from src.persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, legajo):
        super().__init__(nombre, apellido, dni)
        if legajo is None:
            raise ValueError("El legajo no puede ser None")
        if int(legajo) < 0:
            raise ValueError("El legajo no puede ser negativo")
        self.legajo = legajo

    def __repr__(self):
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"
    
    def recibir_idea(self,idea):
        self.pensar(idea)
    
    def compartir_idea(self,persona,idea):
        persona.ultima_idea = idea
