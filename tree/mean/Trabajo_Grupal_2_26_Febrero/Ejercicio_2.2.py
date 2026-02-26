"""
Ejercicio 2.2: Página 66: Definición de atributos de una clase con tipos primitivos de datos
Este módulo modela el concepto de un planeta del sistema solar,
incluyendo atributos de diferentes tipos primitivos (adaptados a Python)
y métodos para calcular su densidad y determinar si es un planeta exterior.
"""

from enum import Enum

class TipoPlaneta(Enum):
    """
    Enumeración para los tipos de planeta según su tamaño.
    """
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    """
    Clase que modela un planeta del sistema solar.
    """
    # Constante para la Unidad Astronómica en Kilómetros (1 UA)
    UA_KM = 149597870

    def __init__(self, nombre: str = None, cantidad_satelites: int = 0, 
                 masa: float = 0.0, volumen: float = 0.0, 
                 diametro: int = 0, distancia_media_sol: int = 0, 
                 tipo: TipoPlaneta = None, es_observable: bool = False):
        
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa  # En kilogramos
        self.volumen = volumen  # En kilómetros cúbicos
        self.diametro = diametro  # En kilómetros
        self.distancia_media_sol = distancia_media_sol  # En millones de kilómetros
        self.tipo_planeta = tipo
        self.es_observable = es_observable

    def imprimir_atributos(self):
        """
        Imprime en pantalla los valores de los atributos del planeta.
        """
        print(f"\n--- Información del Planeta: {self.nombre} ---")
        print(f"Nombre: {self.nombre}")
        print(f"Satélites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diámetro: {self.diametro} km")
        print(f"Distancia al Sol: {self.distancia_media_sol} millones de km")
        # Mostramos el valor (nombre) del Enum
        print(f"Tipo: {self.tipo_planeta.value if self.tipo_planeta else 'No definido'}")
        print(f"Observable a simple vista: {'Sí' if self.es_observable else 'No'}")

    def calcular_densidad(self):
        """
        Calcula la densidad del planeta (Masa / Volumen).
        """
        if self.volumen == 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        """
        Determina si el planeta es exterior (más allá del cinturón de asteroides).
        El cinturón está entre 2.1 y 3.4 UA. Se considera exterior si > 3.4 UA.
        """
        # Convertimos la distancia de millones de km a km normales
        distancia_km = self.distancia_media_sol * 1_000_000
        
        # Calculamos las Unidades Astronómicas
        ua = distancia_km / self.UA_KM
        
        # Si la distancia en UA es mayor al límite del cinturón de asteroides (3.4)
        if ua > 3.4:
            return True
        else:
            return False

def main():
    print("=== SISTEMA ASTRONÓMICO SOLAR ===")
    planetas = []

    # Se crean dos planetas mediante captura de datos
    for i in range(1, 3):
        print(f"\n>>> Ingresando datos del Planeta {i} <<<")
        
        nombre = input("Nombre del planeta: ")
        
        # Validaciones de entrada numérica
        while True:
            try:
                satelites = int(input("Cantidad de satélites: "))
                masa = float(input("Masa (kg): "))
                volumen = float(input("Volumen (km³): "))
                diametro = int(input("Diámetro (km): "))
                distancia = int(input("Distancia media al Sol (en millones de km): "))
                break
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        # Selección del tipo de planeta (Enum)
        print("Seleccione el tipo de planeta:")
        print("1. GASEOSO")
        print("2. TERRESTRE")
        print("3. ENANO")
        while True:
            opcion = input("Opción (1-3): ")
            if opcion == '1':
                tipo = TipoPlaneta.GASEOSO
                break
            elif opcion == '2':
                tipo = TipoPlaneta.TERRESTRE
                break
            elif opcion == '3':
                tipo = TipoPlaneta.ENANO
                break
            else:
                print("Opción no válida.")

        # Selección booleana
        obs_input = input("¿Es observable a simple vista? (S/N): ").strip().upper()
        es_observable = True if obs_input == 'S' else False

        # Instanciamos el objeto
        nuevo_planeta = Planeta(nombre, satelites, masa, volumen, diametro, distancia, tipo, es_observable)
        planetas.append(nuevo_planeta)

    # Mostrar resultados
    print("\n" + "="*40)
    print("       RESULTADOS DEL ANÁLISIS")
    print("="*40)
    
    for p in planetas:
        p.imprimir_atributos()
        print(f"Densidad: {p.calcular_densidad():.4f} kg/km³")
        
        es_ext = p.es_planeta_exterior()
        estado = "EXTERIOR" if es_ext else "INTERIOR (o en el cinturón)"
        print(f"Clasificación por distancia: Planeta {estado}")
        print("-" * 30)

if __name__ == "__main__":
    main()