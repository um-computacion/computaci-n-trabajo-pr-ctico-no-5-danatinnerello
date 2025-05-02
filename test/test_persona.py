import unittest
from src.persona import Persona
from src.alumno import Alumno
class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        """Verifica la correcta creación de un objeto Persona.
        
        Comprueba que los atributos nombre, apellido y dni
        se asignen correctamente al crear una instancia de Persona.
        
        Returns:
            None
        """
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")

    def test_repr_persona(self):
        """Verifica la representación en string de un objeto Persona.
        
        Comprueba que el método __str__ devuelva la cadena esperada
        con el formato "Persona: DNI: X Nombre: Y Apellido: Z Ultima Idea: ".
        
        Returns:
            None
        """
        persona = Persona("Juan", "Pérez", "12345678")
        expected = "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Ultima Idea: "
        self.assertEqual(str(persona), expected)
    
    def test_pensar_incrementa_contador(self):
       """Verifica que el método pensar incremente el contador de pensamientos.
        
        Comprueba que después de llamar al método pensar, el atributo
        pensamientos aumente en 1.
        
        Returns:
            None
        """
       persona = Persona("Juan", "Pérez", "12345678")
       persona.pensar("Hola mundo")
       self.assertEqual(persona.pensamientos, 1)

    def test_pensar_actualiza_ultima_idea(self):
       """Verifica que el método pensar actualice la última idea.
        
        Comprueba que después de llamar al método pensar con una idea,
        el atributo ultima_idea contenga dicha idea.
        
        Returns:
            None
        """
       persona = Persona("Juan", "Pérez", "12345678")
       persona.pensar("Hola mundo")
       self.assertEqual(persona.ultima_idea, "Hola mundo")
    #caso limite 
    def test_persona_con_nombre_vacio(self):
        """Verifica que se lance una excepción al crear una persona con nombre vacío.
        
        Caso límite: Comprueba que la clase Persona valide que el nombre
        no sea una cadena vacía y lance ValueError en caso contrario.
        
        Raises:
            ValueError: Se espera que la clase Persona lance esta excepción.
        
        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Persona("","perez",43213234)
    #validacion de datos
    def test_persona_con_nombre_no_es_cadena(self):
        """Verifica que se lance una excepción cuando el nombre no es una cadena.
        
        Validación de datos: Comprueba que la clase Persona valide que el nombre
        sea una cadena de texto y lance ValueError en caso contrario.
        
        Raises:
            ValueError: Se espera que la clase Persona lance esta excepción.
        
        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Persona(12345,"perez",45678923)
    #interaccion entre clases
    def test_alumno_comparte_idea_con_persona(self):
        """Verifica la interacción entre las clases Alumno y Persona.
        
        Comprueba que un Alumno pueda compartir correctamente una idea
        con una Persona a través del método compartir_idea.
        
        Returns:
            None
        """
        alumno = Alumno("Sofía","perez",45678965, 1234)
        persona = Persona("Diego","lopez",20897564)

        alumno.compartir_idea(persona,"Idea brillante")

        self.assertEqual(persona.ultima_idea, "Idea brillante")