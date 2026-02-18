"""
Ejercicio 2.1, Página 63: Definición de clases (Clase Persona)
Lenguaje: Python
"""

# ---------------------------------------------------------
# ENUNCIADO: Clase Persona
# ---------------------------------------------------------
# Se requiere un programa que modele el concepto de una persona. 
# Una persona posee:
# - Nombre
# - Apellido
# - Número de documento de identidad
# - Año de nacimiento
#
# La clase debe tener un constructor que inicialice los valores de sus respectivos atributos.
#
# La clase debe incluir los siguientes métodos:
# 1. Definir un método que imprima en pantalla los valores de los atributos del objeto.
# 2. En un método main se deben crear dos personas y mostrar los valores de sus atributos en pantalla.

class Persona:
    """
    Clase que define objetos de tipo Persona.
    """
    def __init__(self, nombre: str, apellido: str, documento: str, anio_nacimiento: int):
        """
        Constructor de la clase Persona.
        Inicializa los atributos del objeto.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir_datos(self):
        """
        Método que imprime en pantalla los valores de los atributos del objeto.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Documento: {self.documento}")
        print(f"Año de nacimiento: {self.anio_nacimiento}")
        print("-" * 30)

def main():
    print("--- EJECUCIÓN DEL EJERCICIO 2.1: Clase Persona ---")
    print("")

    # Crear dos objetos de la clase Persona (Instanciación)
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    p2 = Persona("Luis", "León", "1053223344", 2001)

    # Mostrar los valores de sus atributos en pantalla
    print("--- Datos de la Persona 1 ---")
    p1.imprimir_datos()

    print("--- Datos de la Persona 2 ---")
    p2.imprimir_datos()

if __name__ == "__main__":
    main()