"""
Ejercicio 4.6: Métodos Polimórficos
Demostración de la diferencia entre el tipado estático (Java)
y el tipado dinámico de Python al invocar métodos de subclases.
"""

class Profesor:
    """Superclase que representa un profesor genérico."""
    def imprimir(self):
        print("Es un profesor.")

class ProfesorTitular(Profesor):
    """Subclase que hereda de Profesor e incluye un atributo nuevo."""
    def __init__(self):
        # Atributo específico de la clase hija
        self.anos = 0
        
    def imprimir(self):
        print("Es un profesor titular.")
        
    def imprimir_anos(self):
        """Método exclusivo de la subclase."""
        print(f"Años = {self.anos}")

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (Método main)
# ==========================================
if __name__ == "__main__":
    # Se instancia un ProfesorTitular. En Python las variables no declaran su tipo base
    profesor1 = ProfesorTitular()
    
    # En Java esto daría error de compilación.
    # En Python, como el objeto en memoria es ProfesorTitular,
    # encuentra el método imprimir_anos() dinámicamente y lo ejecuta con éxito.
    print("-" * 50)
    print("Ejecutando método exclusivo desde la instancia:")
    profesor1.imprimir_anos()
    print("-" * 50)
