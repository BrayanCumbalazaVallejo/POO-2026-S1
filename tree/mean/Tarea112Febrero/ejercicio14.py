"""
Ejercicio Propuesto No 14

Elabore un algoritmo que lea un número y obtenga su cuadrado y su cubo.
"""

import sys

class Calculadora:
    """
    Clase simple para realizar operaciones matemáticas
    básicas como cuadrado y cubo de un número.
    """
    def __init__(self):
        self.numero = 0.0

    def leer_numero(self):
        try:
            print("Ingrese un número para calcular su cuadrado y cubo: ")
            # Se usa sys.stdin.readline() para asegurar compatibilidad en diferentes entornos
            input_data = sys.stdin.readline().strip()
            if not input_data:
                # Si no hay entrada (ej. ejecución automatizada), se usa un valor por defecto
                self.numero = 5.0  
                print(f"Usando valor por defecto: {self.numero}")
            else:
                self.numero = float(input_data)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un valor numérico. Usando 0 por defecto.")
            self.numero = 0.0

    def calcular_potencias(self):
        # El cuadrado es el número elevado a la 2
        cuadrado = self.numero ** 2
        # El cubo es el número elevado a la 3
        cubo = self.numero ** 3
        
        print(f"\nResultados para el número: {self.numero}")
        print("-" * 35)
        print(f"El cuadrado de {self.numero} es: {cuadrado}")
        print(f"El cubo de {self.numero} es: {cubo}")

if __name__ == "__main__":
    calc = Calculadora()
    calc.leer_numero()
    calc.calcular_potencias()