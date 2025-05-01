import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")

    def test_repr_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        expected = "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Ultima Idea: <no penso en nada>"
        self.assertEqual(str(persona), expected)
    
    def test_pensar_incrementa_contador(self):
       persona = Persona("Juan", "Pérez", "12345678")
       persona.pensar("Hola mundo")
       self.assertEqual(persona.pensamientos, 1)

    def test_pensar_actualiza_ultima_idea(self):
       persona = Persona("Juan", "Pérez", "12345678")
       persona.pensar("Hola mundo")
       self.assertEqual(persona.ultima_idea, "Hola mundo")
    #caso limite 
    def test_persona_con_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Persona("","perez",43213234)
    #validacion de datos
    def test_persona_con_nombre_no_es_cadena(self):
        with self.assertRaises(TypeError):
            Persona(12345,"perez",45678923)
    #interaccion entre clases
    def test_alumno_comparte_idea_con_persona(self):
        alumno = Alumno("Sofía", 1234)
        persona = Persona("Diego")

        alumno.pensar("Idea brillante")
        alumno.compartir_idea(persona)

        self.assertEqual(persona.ultima_idea(), "Idea brillante")