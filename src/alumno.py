from src.persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, legajo):
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo

    def __repr__(self):
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"