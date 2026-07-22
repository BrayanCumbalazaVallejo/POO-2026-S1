"""
Ejercicio 4.4: Polimorfismo
Demostración de sobreescritura de métodos y polimorfismo en Python.
"""

class Profesor:
    """Superclase que representa un profesor genérico."""
    
    def imprimir(self):
        """Método que identifica que el objeto es un Profesor."""
        print("Es un profesor.")

class ProfesorTitular(Profesor):
    """Subclase que hereda de Profesor."""
    
    def imprimir(self):
        """Método que sobreescribe el comportamiento de la clase padre."""
        print("Es un profesor titular.")

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (Método main)
# ==========================================
if __name__ == "__main__":
    # Se declara la variable instanciando la clase hija
    profesor1 = ProfesorTitular()
    
    # Se invoca el método. Por polimorfismo, ejecutará el de la clase hija.
    profesor1.imprimir()
