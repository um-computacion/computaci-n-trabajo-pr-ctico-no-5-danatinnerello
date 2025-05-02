# Sistema de Gestión Académica

Este proyecto implementa un sistema simple de gestión académica que modela las interacciones entre `Persona`, `Alumno` y `Profesor`. El sistema permite la creación de estos objetos y la simulación de interacciones educativas como enseñar, aprender y compartir ideas.

## Estructura del Proyecto

```

├── src/
│   ├── __init__.py
│   ├── persona.py      # Clase base que define una persona
│   ├── alumno.py       # Clase que hereda de Persona
│   └── profesor.py     # Clase que hereda de Persona
    └── ejemplo_uso.py      # Script de ejemplo que demuestra el uso del sistema
├── tests/
│   ├── __init__.py
│   ├── test_persona.py    # Tests para la clase Persona
│   ├── test_alumno.py     # Tests para la clase Alumno
│   └── test_profesor.py   # Tests para la clase Profesor
```

## Ejecución

### Ejecutar el ejemplo de uso

El archivo `ejemplo_uso.py` demuestra cómo utilizar las clases del sistema:

```bash
python3 ejemplo_uso.py
```

### Ejecutar los tests

Para ejecutar todos los tests:

```bash
python -m unittest discover tests
```

Para ejecutar un archivo de test específico:

```bash
python -m unittest tests/test_persona.py
python -m unittest tests/test_alumno.py
python -m unittest tests/test_profesor.py
```

## Descripción de las Clases

### Persona
- Clase base que representa a una persona con nombre, apellido y DNI
- Puede pensar y almacenar ideas

### Alumno (hereda de Persona)
- Representa a un estudiante con un número de legajo
- Puede recibir ideas de profesores
- Puede compartir ideas con otras personas

### Profesor (hereda de Persona)
- Representa a un docente con un sueldo
- Puede enseñar ideas
- Puede responder preguntas

## Ejemplos de Uso

El archivo `ejemplo_uso.py` incluye ejemplos de:
- Creación de personas, alumnos y profesores
- Uso del método `pensar` en personas
- Profesores enseñando ideas
- Alumnos recibiendo ideas
- Profesores respondiendo preguntas
- Alumnos compartiendo ideas
- Cadena completa de transmisión de conocimiento

## Testing

El proyecto incluye tests unitarios para todas las clases, incluidos:
- Tests básicos de creación de objetos
- Tests de representación de cadenas (__repr__)
- Tests de casos límite (valores vacíos, negativos)
- Tests de validación de datos
- Tests de interacción entre clases