import unittest
from src.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_crear_alumno(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.dni, "12345678")
        self.assertEqual(alumno.legajo, "A123")

    def test_repr_alumno(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        expected = "Alumno: DNI: 12345678 Nombre: Juan Apellido: Pérez Legajo: A123"
        self.assertEqual(str(alumno), expected)
    #casos limite 
    def test_alumno_con_legajo_negativo(self):
        with self.assertRaises(ValueError):
            Alumno("Maria","Garcia",40657890,-123)
    #validacion de datos 
    def test_alumno_legajo_no_numerico(self):
        with self.assertRiases(TypeError):
            Alumno("Maria","Perez",56432678,"agf45")
    #interaccion entre clases 
    def test_alumno_recibe_idea_de_profesor(self):
        profesor = Profesor("Luis", "Historia", 50000)
        alumno = Alumno("Ana", 1001)

        profesor.enseñar("La Revolución Francesa")
        alumno.recibir_idea(profesor.ultima_idea())

        self.assertEqual(alumno.ultima_idea(), "La Revolución Francesa")