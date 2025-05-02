"""
Ejemplo de uso del sistema de gestión académica con Personas, Alumnos y Profesores.

Este codigo muestra cómo utilizar e interactuar con las clases Persona, Alumno y Profesor
en diferentes escenarios educativos.
"""
from src.persona import Persona
from src.alumno import Alumno
from src.profesor import Profesor

def main():
    # ----- Creación de objetos -----
    
    # Creamos algunas personas
    ana = Persona("Ana", "García", 30456789)
    carlos = Persona("Carlos", "Mendez", 28765432)
    
    print(f"Persona creada: {ana}")
    print(f"Persona creada: {carlos}")
    
    # Creamos algunos profesores
    laura = Profesor("Laura", "Martinez", 25678901, 65000)
    miguel = Profesor("Miguel", "Rodriguez", 27891234, 58000)
    
    print(f"Profesor creado: {laura}")
    print(f"Profesor creado: {miguel}")
    
    # Creamos algunos alumnos
    juan = Alumno("Juan", "Perez", 40123456, 1001)
    maria = Alumno("Maria", "Lopez", 39876543, 1002)
    sofia = Alumno("Sofia", "Gonzalez", 41234567, 1003)
    
    print(f"Alumno creado: {juan}")
    print(f"Alumno creado: {maria}")
    print(f"Alumno creado: {sofia}")
    
    # ----- Demostración de funcionalidad -----
    
    # Ejemplo de pensar
    ana.pensar("Los planetas giran alrededor del sol")
    print(f"Ana pensó una idea. Pensamientos acumulados: {ana.pensamientos}")
    print(f"La última idea de Ana es: '{ana.ultima_idea}'")
    
    # Ejemplo de profesores enseñanando
    laura.enseñar("La fotosíntesis es el proceso por el cual las plantas convierten luz en energía")
    miguel.enseñar("La Segunda Guerra Mundial ocurrió entre 1939 y 1945")
    
    print(f"Laura enseñó: '{laura.ultima_idea}'")
    print(f"Miguel enseñó: '{miguel.ultima_idea}'")
    
    # Alumnos recibiendo ideas de profesores
    juan.recibir_idea(laura.ultima_idea)
    maria.recibir_idea(miguel.ultima_idea)
    
    print(f"Juan recibió la idea: '{juan.ultima_idea}'")
    print(f"María recibió la idea: '{maria.ultima_idea}'")
    
    # Profesores respondiendo pregunta
    respuesta1 = laura.responder("¿Por qué el cielo es azul?")
    respuesta2 = miguel.responder("¿Cuáles son las causas del cambio climático?")
    
    print(f"Respuesta de Laura: {respuesta1}")
    print(f"Respuesta de Miguel: {respuesta2}")
    
    # Alumnos compartiendo ideas con personas
    sofia.pensar("La inteligencia artificial transformará el futuro de la educación")
    sofia.compartir_idea(carlos, sofia.ultima_idea)
    
    print(f"Sofía pensó: '{sofia.ultima_idea}'")
    print(f"Sofía compartió su idea con Carlos")
    print(f"Ahora Carlos tiene la idea: '{carlos.ultima_idea}'")
    
    # Cadena de transmisión de conocimiento
    # El profesor enseña
    laura.enseñar("El teorema de Pitágoras establece que a² + b² = c²")
    print(f"La profesora Laura enseña: '{laura.ultima_idea}'")
    
    # El alumno recibe la idea
    juan.recibir_idea(laura.ultima_idea)
    print(f"Juan recibe la idea: '{juan.ultima_idea}'")
    
    # El alumno comparte la idea con otra persona
    juan.compartir_idea(ana, juan.ultima_idea)
    print(f"Juan comparte la idea con Ana")
    print(f"Ahora Ana tiene la idea: '{ana.ultima_idea}'")

if __name__ == "__main__":
    main()
