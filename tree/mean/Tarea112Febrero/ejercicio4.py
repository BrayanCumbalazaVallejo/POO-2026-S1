"""
Ejercicio resuelto Nº 4

A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele a Juan su
edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la edad de Juan y mi edad es
la suma de las tres. Hacer un algoritmo que muestre la edad de los cuatro.
"""

import sys

class Familia:
    """
    Clase que representa a la familia y calcula las edades
    basadas en la edad de Juan.
    """
    def __init__(self):
        self.edad_juan = 0
        self.edad_alberto = 0.0
        self.edad_ana = 0.0
        self.edad_mama = 0.0

    def solicitar_datos(self):
        try:
            print("Ingrese la edad de Juan: ")
            # Leemos la entrada estándar
            input_data = sys.stdin.readline()
            if not input_data:
                # Valor por defecto para pruebas si no hay entrada
                self.edad_juan = 9 
                print(f"Usando valor por defecto: {self.edad_juan}")
            else:
                self.edad_juan = int(input_data)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    def calcular_edades(self):
        # Alberto tiene 2/3 de la edad de Juan
        self.edad_alberto = (2/3) * self.edad_juan
        
        # Ana tiene 4/3 de la edad de Juan
        self.edad_ana = (4/3) * self.edad_juan
        
        # La mamá tiene la suma de las tres edades
        self.edad_mama = self.edad_juan + self.edad_alberto + self.edad_ana

    def mostrar_resultados(self):
        print(f"La edad de Juan es: {self.edad_juan}")
        print(f"La edad de Alberto es: {self.edad_alberto:.0f}")
        print(f"La edad de Ana es: {self.edad_ana:.0f}")
        print(f"La edad de la Mamá es: {self.edad_mama:.0f}")

if __name__ == "__main__":
    familia = Familia()
    familia.solicitar_datos()
    familia.calcular_edades()
    familia.mostrar_resultados()