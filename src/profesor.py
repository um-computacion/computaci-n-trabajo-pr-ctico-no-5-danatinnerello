from src.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, sueldo):
        super().__init__(nombre, apellido, dni)
        if not apellido:
            raise ValueError("El apellido no puede estar vacio")
        if sueldo < 0:
            raise ValueError("el sueldo no puede ser negativo")
        self.sueldo = sueldo

    def __repr__(self):
        return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"
    def responder(self,pregunta):
        return f"buena pregunta:{pregunta}"
    def enseñar(self,idea):
        self.ultima_idea = idea 