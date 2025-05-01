
class Persona:
    def __init__(self, nombre, apellido, dni):
        if not nombre:
            raise ValueError("El nombre no puede estar vacio")
        if not isinstance(nombre,str):
            raise ValueError("el nombre debe ser una cadena de texto")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = ""

    def __repr__(self):
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
        
    def pensar(self, idea):
        self.pensamientos += 1
        self.ultima_idea = idea