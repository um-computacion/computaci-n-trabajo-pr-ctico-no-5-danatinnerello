import unittest
from src.profesor import Profesor

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
    def test_alumno_pregunta_profesor_responde(self):
        alumno = Alumno("Martín", 2023)
        profesor = Profesor("Laura", "Matemática", 70000)

        pregunta = "¿Qué es una función?"
        respuesta = profesor.responder(pregunta)

        self.assertEqual(respuesta, "Buena pregunta: ¿Qué es una función?")