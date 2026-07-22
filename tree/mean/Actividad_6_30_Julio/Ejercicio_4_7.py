"""
Ejercicio 4.7: Clases Abstractas
Jerarquía taxonómica de animales utilizando el módulo abc de Python.
"""
from abc import ABC, abstractmethod

# ==========================================
# CLASES ABSTRACTAS
# ==========================================
class Animal(ABC):
    """Clase raíz abstracta que define la estructura base para los animales."""
    
    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass

class Canido(Animal):
    """Subclase abstracta intermedia para los cánidos."""
    pass

class Felino(Animal):
    """Subclase abstracta intermedia para los felinos."""
    pass


# ==========================================
# CLASES CONCRETAS
# ==========================================
class Perro(Canido):
    def get_nombre_cientifico(self):
        return "Canis lupus familiaris"
    
    def get_sonido(self):
        return "Ladrido"
    
    def get_alimentos(self):
        return "Carnívora"
    
    def get_habitat(self):
        return "Doméstico"

class Lobo(Canido):
    def get_nombre_cientifico(self):
        return "Canis lupus"
    
    def get_sonido(self):
        return "Aullido"
    
    def get_alimentos(self):
        return "Carnívora"
    
    def get_habitat(self):
        return "Bosque"

class Leon(Felino):
    def get_nombre_cientifico(self):
        return "Panthera leo"
    
    def get_sonido(self):
        return "Rugido"
    
    def get_alimentos(self):
        return "Carnívora"
    
    def get_habitat(self):
        return "Pradera"

class Gato(Felino):
    def get_nombre_cientifico(self):
        return "Felis silvestris catus"
    
    def get_sonido(self):
        return "Maullido"
    
    def get_alimentos(self):
        return "Ratones"
    
    def get_habitat(self):
        return "Doméstico"


# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (Método main)
# ==========================================
if __name__ == "__main__":
    # 1. Generar un array (lista en Python) de animales instanciados
    array_animales = [Perro(), Lobo(), Leon(), Gato()]
    
    print("=" * 50)
    print("        SISTEMA DE INFORMACIÓN TAXONÓMICA")
    print("=" * 50)
    
    # 2. Recorrer el array mostrando los valores de sus atributos
    for animal in array_animales:
        # animal.__class__.__name__ obtiene el nombre de la clase hija en ejecución
        print(f"Tipo de Animal:    {animal.__class__.__name__}")
        print(f"Nombre Científico: {animal.get_nombre_cientifico()}")
        print(f"Sonido:            {animal.get_sonido()}")
        print(f"Alimentación:      {animal.get_alimentos()}")
        print(f"Hábitat:           {animal.get_habitat()}")
        print("-" * 50)