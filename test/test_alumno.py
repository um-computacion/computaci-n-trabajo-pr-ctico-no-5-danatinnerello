import unittest
from src.alumno import Alumno
from src.profesor import Profesor

class TestAlumno(unittest.TestCase):
    def test_crear_alumno(self):
        """Verifica la correcta creación de un objeto Alumno.
        
        Comprueba que los atributos nombre, apellido, dni y legajo
        se asignen correctamente al crear una instancia de Alumno.
        
        Returns:
            None
        """
        alumno = Alumno("Juan", "Pérez", "12345678", "123")
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.dni, "12345678")
        self.assertEqual(alumno.legajo, "123")

    def test_repr_alumno(self):
        """Verifica la representación en string de un objeto Alumno.
        
        Comprueba que el método __str__ devuelva la cadena esperada
        con el formato "Alumno: DNI: X Nombre: Y Apellido: Z Legajo: W".
        
        Returns:
            None
        """
        alumno = Alumno("Juan", "Pérez", "12345678", "123")
        expected = "Alumno: DNI: 12345678 Nombre: Juan Apellido: Pérez Legajo: 123"
        self.assertEqual(str(alumno), expected)
    #casos limite 
    def test_alumno_con_legajo_negativo(self):
        """Verifica que se lance una excepción al crear un alumno con legajo negativo.
        
        Caso límite: Comprueba que la clase Alumno valide que el legajo
        no sea un número negativo y lance ValueError en caso contrario.
        
        Raises:
            ValueError: Se espera que la clase Alumno lance esta excepción.
        
        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Alumno("Maria","Garcia",40657890,-123)
    #validacion de datos 
    def test_alumno_legajo_vacio(self):
        """Verifica que se lance una excepción al crear un alumno con legajo vacío.
        
        Validación de datos: Comprueba que la clase Alumno valide que el legajo
        no sea una cadena vacía y lance ValueError en caso contrario.
        
        Raises:
            ValueError: Se espera que la clase Alumno lance esta excepción.
        
        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Alumno("Maria","Perez",56432678,"")
    #interaccion entre clases 
    def test_alumno_recibe_idea_de_profesor(self):
        """Verifica la interacción entre las clases Profesor y Alumno.
        
        Comprueba que un alumno pueda recibir correctamente una idea enseñada
        por un profesor a través del método recibir_idea.
        
        Returns:
            None
        """
        profesor = Profesor("Luis", "Gracia", 15678943,50000)
        alumno = Alumno("Ana","Lopez",47653456,1001)

        profesor.enseñar("La Revolución Francesa")
        alumno.recibir_idea(profesor.ultima_idea)

        self.assertEqual(alumno.ultima_idea, "La Revolución Francesa")