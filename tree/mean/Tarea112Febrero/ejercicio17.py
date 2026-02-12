"""
Ejercicio Propuesto No 17

Dado el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la longitud
de la circunferencia.
"""

import math
import sys

class Circulo:
    """
    Clase que representa un círculo y sus propiedades geométricas.
    """
    def __init__(self):
        self.radio = 0.0
        self.area = 0.0
        self.longitud = 0.0

    def leer_radio(self):
        try:
            print("Ingrese el radio del círculo: ")
            # Se usa sys.stdin.readline() para asegurar compatibilidad en diferentes entornos
            input_data = sys.stdin.readline().strip()
            if not input_data:
                # Si no hay entrada (ej. ejecución automatizada), se usa un valor por defecto
                self.radio = 10.0  
                print(f"Usando valor por defecto: {self.radio}")
            else:
                self.radio = float(input_data)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un valor numérico. Usando 0.0 por defecto.")
            self.radio = 0.0

    def calcular_propiedades(self):
        # Área = pi * r^2
        self.area = math.pi * (self.radio ** 2)
        
        # Longitud (Circunferencia) = 2 * pi * r
        self.longitud = 2 * math.pi * self.radio

    def mostrar_resultados(self):
        print(f"\nResultados para el círculo de radio: {self.radio}")
        print("-" * 45)
        print(f"Área del círculo:              {self.area:.4f}")
        print(f"Longitud de la circunferencia: {self.longitud:.4f}")

if __name__ == "__main__":
    mi_circulo = Circulo()
    mi_circulo.leer_radio()
    mi_circulo.calcular_propiedades()
    mi_circulo.mostrar_resultados()