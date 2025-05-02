
class Persona:
    '''
        Representa una persona con sus respetivos atributos

        Atributos:
        nombre(str): el nombre de la persona
        apellido (str): el apellido de la persona
        dni(int): el dni de la persona
        '''
    def __init__(self, nombre, apellido, dni):
        '''
        Inicializa a una persona con un nombre, apellido y dni
        '''
        if not nombre:
            raise ValueError("El nombre no puede estar vacio")
        ''' verifica que la persona ingrese algo en el campo de nombre
        '''
        if not isinstance(nombre,str):
            raise ValueError("el nombre debe ser una cadena de texto")
        ''' verifica que la persona inggrese una cadena de texto y no otra cosa como numeros 
        '''
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = ""

    def __repr__(self):
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
    '''
    define como se muestra un objeto cuando lo imprimis
    '''
    def pensar(self, idea):
        self.pensamientos += 1
        self.ultima_idea = idea
    '''
    guarda una idea pensada por la persona
    suma un pensamiento
    argumento:
    idea(str): la idea a guardar

    '''