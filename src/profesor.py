from src.persona import Persona

class Profesor(Persona):
    """
    Representa a un profesor con información personal y habilidades para enseñar y responder ideas.

    Atributos:
        nombre(str): Nombre del profesor.
        apellido(str): Apellido del profesor.
        dni(int): Documento Nacional de Identidad del profesor.
        sueldo(float): Sueldo del profesor.
        ultima_idea(str): Última idea enseñada o respondida por el profesor.
    """
    def __init__(self, nombre, apellido, dni, sueldo):
        """
        Inicializa un nuevo objeto Profesor.

        Argumentos:
            nombre(str): Nombre del profesor.
            apellido(str): Apellido del profesor.
            dni(int): DNI del profesor.
            sueldo(float): Sueldo del profesor.
        Raises:
            ValueError: Si alguno de los parámetros no tiene el tipo adecuado.
        """
        super().__init__(nombre, apellido, dni)
        if not apellido:
            raise ValueError("El apellido no puede estar vacio")
        if sueldo < 0:
            raise ValueError("el sueldo no puede ser negativo")
        self.sueldo = sueldo

    def __repr__(self):
        """
        Devuelve una representación legible del objeto profesor.
        """
        return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"
    def responder(self,pregunta):
        """
        Responde una pregunta

        Argumento:
            pregunta(str): pregunta que responde recursivamente.
        """
        return f"buena pregunta:{pregunta}"
    def enseñar(self,idea):
        """
        Enseña una idea, registrándola como la última idea del profesor.
        Argumento:
            idea(str): Idea que enseña el profesor.
        """
        self.ultima_idea = idea 