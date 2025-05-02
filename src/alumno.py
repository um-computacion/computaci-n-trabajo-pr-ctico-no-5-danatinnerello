from src.persona import Persona

class Alumno(Persona):
    """
    Representa a un alumno con información personal y capacidad para compartir ideas.

    Atributos:
        nombre(str):Nombre del alumno.
        apellido(str):Apellido del alumno.
        dni (int):Documento Nacional de Identidad del alumno.
        legajo(int):Número de legajo del alumno.
        ultima_idea(str):Última idea recibida o compartida por el alumno.
    """
    def __init__(self, nombre, apellido, dni, legajo):
        """
        Inicializa un nuevo alumno.
        Argumentos:
            nombre str):Nombre del alumno.
            apellido(str):Apellido del alumno.
            dni(int):DNI del alumno.
            legajo(int):Legajo del alumno.
        Raises:
            ValueError: Si alguno de los valores no cumple con los tipos esperados.
        """
        super().__init__(nombre, apellido, dni)
        if legajo is None:
            raise ValueError("El legajo no puede ser None")
        if int(legajo) < 0:
            raise ValueError("El legajo no puede ser negativo")
        self.legajo = legajo

    def __repr__(self):
        """
        Devuelve una representación legible del objeto alumno.
        """
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"
    
    def recibir_idea(self,idea):
        """
        Recibe una idea y la guarda como la última idea del alumno.
        Argumento:
            idea (str): Idea recibida.
        """
        self.pensar(idea)
    
    def compartir_idea(self,persona,idea):
        persona.ultima_idea = idea
