import unittest
from src.profesor import Profesor
from src.alumno import Alumno

class TestProfesor(unittest.TestCase):
    def test_crear_profesor(self):
        """Verifica la correcta creación de un objeto Profesor.
        
        Comprueba que los atributos nombre, apellido, dni y sueldo
        se asignen correctamente al crear una instancia de Profesor.
        
        Returns:
            None
        """
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        self.assertEqual(profesor.nombre, "Juan")
        self.assertEqual(profesor.apellido, "Pérez")
        self.assertEqual(profesor.dni, "12345678")
        self.assertEqual(profesor.sueldo, 50000)

    def test_repr_profesor(self):
        """Verifica la representación en string de un objeto Profesor.
        
        Comprueba que el método __str__ devuelva la cadena esperada
        con el formato "Profesor: DNI: X Nombre: Y Apellido: Z Sueldo: W".
        
        Returns:
            None
        """
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        expected = "Profesor: DNI: 12345678 Nombre: Juan Apellido: Pérez Sueldo: 50000"
        self.assertEqual(str(profesor), expected)
    #caso limite 
    def test_profesor_sin_apellido(self):
        """Verifica que se lance una excepción al crear un profesor sin apellido.
        
        Caso límite: Comprueba que la clase Profesor valide que el apellido
        no sea una cadena vacía y lance ValueError en caso contrario.
        
        Raises:
            ValueError: Se espera que la clase Profesor lance esta excepción.
        
        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Profesor("Luis","",20654321,50000)
    #validacion de datos
    def test_profesor_con_sueldo_negativo(self):
        """Verifica que se lance una excepción al crear un profesor con sueldo negativo.
        
        Validación de datos: Comprueba que la clase Profesor valide que el sueldo
        no sea un número negativo y lance ValueError en caso contrario.
        
        Raises:
            ValueError: Se espera que la clase Profesor lance esta excepción.
        
        Returns:
            None
        """
        with self.assertRaises(ValueError):
            Profesor("Luis","Perez",20564321,-50000)
    #interaccion entre clases 
    def test_profesor_responde_pregunta(self):
       """Verifica que el profesor responda correctamente a una pregunta.
        
        Interacción entre clases: Comprueba que el método responder de Profesor
        devuelve la respuesta con el formato "buena pregunta:[pregunta]".
        
        Returns:
            None
        """
       profesor = Profesor("Elena", "Diaz",21345634, 58000)
       respuesta = profesor.responder("¿Qué es un poema?")
       self.assertEqual(respuesta, "buena pregunta:¿Qué es un poema?")