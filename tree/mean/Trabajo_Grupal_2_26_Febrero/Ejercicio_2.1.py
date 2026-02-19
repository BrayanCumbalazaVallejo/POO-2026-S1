"""
Ejercicio 2.1: Página 63: Definición de clases (Clase Persona)
Este módulo modela el concepto de una persona con sus atributos básicos
y permite imprimir su información en pantalla.
"""

class Persona:
    """
    Clase que representa a una persona.
    """

    def __init__(self, nombre: str, apellidos: str, numero_documento_identidad: str, año_nacimiento: int):
        """
        Constructor de la clase Persona. Inicializa los atributos de la persona.
        
        Parámetros:
        nombre (str): El nombre de la persona.
        apellidos (str): Los apellidos de la persona.
        numero_documento_identidad (str): El número de documento de identidad.
        año_nacimiento (int): El año de nacimiento de la persona.
        """
        # En Python, 'self' cumple la misma función que 'this' en Java
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.año_nacimiento = año_nacimiento

    def imprimir(self):
        """
        Imprime en pantalla los valores de los atributos del objeto Persona.
        Corresponde al método void imprimir() del diagrama UML.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Número de Documento de Identidad: {self.numero_documento_identidad}")
        print(f"Año de Nacimiento: {self.año_nacimiento}")
        print("-" * 30) # Línea separadora para mayor claridad en consola


# Método main simulado en Python
if __name__ == "__main__":
    # 1. Se crean dos objetos de la clase Persona
    persona1 = Persona("Brayan", "Cumbalaza Vallejo", "1000123456", 2003)
    persona2 = Persona("Daniel", "Maldonado Zuluaga", "1000654321", 2002)

    # 2. Se muestran los valores de sus atributos en pantalla llamando al método imprimir
    print("--- Información de la Persona 1 ---")
    persona1.imprimir()

    print("--- Información de la Persona 2 ---")
    persona2.imprimir()