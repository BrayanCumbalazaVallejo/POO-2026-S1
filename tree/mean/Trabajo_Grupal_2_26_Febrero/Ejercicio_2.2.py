"""
Ejercicio 2.2, Página 66: Definición de atributos de una clase con tipos primitivos de datos
Lenguaje: Python
"""

from enum import Enum
from typing import Optional

# ---------------------------------------------------------
# ENUNCIADO: Clase Planeta
# ---------------------------------------------------------
# Se requiere un programa que modele el concepto de un planeta del sistema solar.
# Un planeta tiene los siguientes atributos:
# - Un nombre de tipo String con valor inicial de null.
# - Cantidad de satélites de tipo int con valor inicial de cero.
# - Masa en kilogramos de tipo double con valor inicial de cero.
# - Volumen en kilómetros cúbicos de tipo double con valor inicial de cero.
# - Diámetro en kilómetros de tipo int con valor inicial de cero.
# - Distancia media al Sol en millones de kilómetros, de tipo int con valor inicial de cero.
# - Tipo de planeta de acuerdo con su tamaño (GASEOSO, TERRESTRE, ENANO).
# - Observable a simple vista, de tipo booleano con valor inicial false.
#
# La clase debe incluir:
# 1. Constructor que inicialice los valores.
# 2. Método imprimir() para mostrar atributos.
# 3. Calcular densidad (masa / volumen).
# 4. Determinar si es planeta exterior (> 3.4 UA del cinturón de asteroides).
#    (1 UA = 149,597,870 Km).
# 5. Método main para crear dos planetas e imprimir sus datos.

class TipoPlaneta(Enum):
    """Enumeración para definir los tipos de planeta según su tamaño."""
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    """
    Clase que modela un planeta del sistema solar.
    """
    def __init__(self, 
                 nombre: str = None, 
                 cantidad_satelites: int = 0, 
                 masa: float = 0.0, 
                 volumen: float = 0.0, 
                 diametro: int = 0, 
                 distancia_sol: int = 0, 
                 tipo_planeta: TipoPlaneta = None, 
                 es_observable: bool = False):
        """
        Constructor de la clase Planeta. Inicializa los atributos.
        
        :param distancia_sol: Distancia en millones de kilómetros (int).
        """
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo_planeta = tipo_planeta
        self.es_observable = es_observable

    def imprimir(self):
        """
        Imprime en pantalla los valores de los atributos del planeta.
        """
        tipo_str = self.tipo_planeta.value if self.tipo_planeta else "Desconocido"
        observable_str = "Sí" if self.es_observable else "No"
        
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diámetro: {self.diametro} km")
        print(f"Distancia media al Sol: {self.distancia_sol} millones de km")
        print(f"Tipo de planeta: {tipo_str}")
        print(f"Es observable a simple vista: {observable_str}")

    def calcular_densidad(self) -> float:
        """
        Calcula la densidad del planeta como el cociente entre su masa y su volumen.
        Retorna 0.0 si el volumen es 0 para evitar división por cero.
        """
        if self.volumen != 0:
            return self.masa / self.volumen
        return 0.0

    def es_planeta_exterior(self) -> bool:
        """
        Determina si un planeta del sistema solar se considera exterior.
        Un planeta exterior está situado más allá del cinturón de asteroides.
        El cinturón de asteroides se encuentra entre 2.1 y 3.4 UA.
        Por tanto, se considera exterior si su distancia es > 3.4 UA.
        
        Datos:
        1 UA = 149.597.870 Km.
        self.distancia_sol está en 'millones de km'.
        """
        # Constante dada por el enunciado
        ua_en_km = 149_597_870
        limite_exterior_ua = 3.4
        
        # Calcular el límite en Kilómetros reales
        limite_en_km = limite_exterior_ua * ua_en_km
        
        # Convertir la distancia del planeta (que está en millones) a kilómetros reales
        distancia_planeta_km = self.distancia_sol * 1_000_000
        
        # Comparar
        if distancia_planeta_km > limite_en_km:
            return True
        else:
            return False

def main():
    """
    Método main donde se crean dos planetas y se muestran sus valores.
    """
    print("--- INICIO DEL PROGRAMA ---")

    # Creación del Planeta 1 (Ejemplo: Tierra)
    p1 = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.972e24,
        volumen=1.08321e12,
        diametro=12742,
        distancia_sol=150,  # 150 millones de km
        tipo_planeta=TipoPlaneta.TERRESTRE,
        es_observable=True
    )

    # Creación del Planeta 2 (Ejemplo: Júpiter)
    p2 = Planeta(
        nombre="Júpiter",
        cantidad_satelites=79,
        masa=1.898e27,
        volumen=1.43128e15,
        diametro=139820,
        distancia_sol=750,  # 750 millones de km
        tipo_planeta=TipoPlaneta.GASEOSO,
        es_observable=True
    )

    # Imprimir datos Planeta 1
    print("\n--- Planeta 1 ---")
    p1.imprimir()
    print(f"Densidad: {p1.calcular_densidad():.4e} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if p1.es_planeta_exterior() else 'No'}")

    # Imprimir datos Planeta 2
    print("\n--- Planeta 2 ---")
    p2.imprimir()
    print(f"Densidad: {p2.calcular_densidad():.4e} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if p2.es_planeta_exterior() else 'No'}")

# Punto de entrada de ejecución
if __name__ == "__main__":
    main()