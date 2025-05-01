import unittest
from src.profesor import Profesor
from src.alumno import Alumno

class TestProfesor(unittest.TestCase):
    def test_crear_profesor(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        self.assertEqual(profesor.nombre, "Juan")
        self.assertEqual(profesor.apellido, "Pérez")
        self.assertEqual(profesor.dni, "12345678")
        self.assertEqual(profesor.sueldo, 50000)

    def test_repr_profesor(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        expected = "Profesor: DNI: 12345678 Nombre: Juan Apellido: Pérez Sueldo: 50000"
        self.assertEqual(str(profesor), expected)
    #caso limite 
    def test_profesor_sin_apellido(self):
        with self.assertRaises(ValueError):
            Profesor("Luis","",20654321,50000)
    #validacion de datos
    def profesor_con_sueldo_negativo(self):
        with self.assertRaises(ValueError):
            Profesor("Luis","Perez",20564321,-50000)
    #interaccion entre clases 
    def test_profesor_responde_pregunta(self):
       profesor = Profesor("Elena", "Diaz",21345634, 58000)
       respuesta = profesor.responder("¿Qué es un poema?")
       self.assertEqual(respuesta, "buena pregunta:¿Qué es un poema?")