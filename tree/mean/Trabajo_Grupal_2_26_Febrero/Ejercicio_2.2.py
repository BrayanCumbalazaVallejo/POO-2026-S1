"""
Ejercicio 2.2: Página 66: Definición de atributos de una clase con tipos primitivos de datos
Este módulo modela el concepto de un planeta del sistema solar,
incluyendo atributos de diferentes tipos primitivos (adaptados a Python)
y métodos para calcular su densidad y determinar si es un planeta exterior.
"""

from enum import Enum

class TipoPlaneta(Enum):
    """Enumeración para los tipos de planeta según su tamaño."""
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    """Clase que representa un planeta del sistema solar."""

    def __init__(self, 
                 nombre: str = None, 
                 cantidad_satelites: int = 0, 
                 masa_kilogramos: float = 0.0, 
                 volumen_kilometros_cubicos: float = 0.0, 
                 diametro_kilometros: int = 0, 
                 distancia_media_sol: int = 0, 
                 tipo_planeta: TipoPlaneta = None, 
                 observable_simple_vista: bool = False):
        """
        Constructor de la clase Planeta.
        Se asignan valores por defecto simulando el comportamiento inicial solicitado.
        """
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa_kilogramos = masa_kilogramos
        self.volumen_kilometros_cubicos = volumen_kilometros_cubicos
        self.diametro_kilometros = diametro_kilometros
        self.distancia_media_sol = distancia_media_sol # En millones de kilómetros
        self.tipo_planeta = tipo_planeta
        self.observable_simple_vista = observable_simple_vista

    def imprimir(self):
        """Imprime en pantalla los valores de los atributos del planeta."""
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa (kg): {self.masa_kilogramos}")
        print(f"Volumen (km³): {self.volumen_kilometros_cubicos}")
        print(f"Diámetro (km): {self.diametro_kilometros}")
        print(f"Distancia media al Sol (millones de km): {self.distancia_media_sol}")
        # Se extrae el valor del Enum para que se lea mejor en consola
        tipo = self.tipo_planeta.value if self.tipo_planeta else "Desconocido"
        print(f"Tipo de planeta: {tipo}")
        print(f"Observable a simple vista: {'Sí' if self.observable_simple_vista else 'No'}")

    def calcular_densidad(self) -> float:
        """
        Calcula la densidad del planeta (masa / volumen).
        Retorna:
            float: Densidad del planeta. Retorna 0.0 si el volumen es cero para evitar errores.
        """
        if self.volumen_kilometros_cubicos == 0:
            return 0.0
        return self.masa_kilogramos / self.volumen_kilometros_cubicos

    def es_planeta_exterior(self) -> bool:
        """
        Determina si un planeta es exterior (ubicado más allá del cinturón de asteroides).
        El límite exterior del cinturón es 3.4 UA.
        1 UA = 149,597,870 km = 149.59787 millones de km.
        """
        # Límite en millones de kilómetros: 3.4 * 149.59787
        limite_exterior_millones_km = 3.4 * 149.59787
        
        # Comparamos la distancia del planeta (que ya está en millones de km) con el límite
        return self.distancia_media_sol > limite_exterior_millones_km


# Método main simulado en Python
if __name__ == "__main__":
    # 1. Creación de dos planetas (Júpiter y la Tierra como ejemplos)
    planeta1 = Planeta("Júpiter", 95, 1.898e27, 1.431e15, 139820, 778, TipoPlaneta.GASEOSO, True)
    planeta2 = Planeta("Tierra", 1, 5.972e24, 1.083e12, 12742, 149, TipoPlaneta.TERRESTRE, True)

    # 2. Mostrar atributos, densidad y si es exterior para el Planeta 1
    print("--- Información del Planeta 1 ---")
    planeta1.imprimir()
    print(f"Densidad: {planeta1.calcular_densidad():.2e} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if planeta1.es_planeta_exterior() else 'No'}")
    print("\n")

    # 3. Mostrar atributos, densidad y si es exterior para el Planeta 2
    print("--- Información del Planeta 2 ---")
    planeta2.imprimir()
    print(f"Densidad: {planeta2.calcular_densidad():.2e} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if planeta2.es_planeta_exterior() else 'No'}")