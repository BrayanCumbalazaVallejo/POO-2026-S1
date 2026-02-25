"""
Ejercicio resuelto N° 5

Hacer un seguimiento (prueba de escritorio) del siguiente grupo de instrucciones.
INICIO
SUMA = 0
X = 20
SUMA = SUMA + X
Y = 40
X = X + Y^2
SUMA = SUMA + X/Y
ESCRIBA: "EL VALOR DE LA SUMA ES:", SUMA
FIN_INICIO
"""

class PruebaEscritorio:
    """
    Clase para realizar el seguimiento del algoritmo dado
    en el Ejercicio Resuelto No 5.
    """
    def __init__(self):
        self.suma = 0
        self.x = 0
        self.y = 0

    def ejecutar_algoritmo(self):
        # SUMA = 0
        self.suma = 0
        print(f"Inicio: SUMA = {self.suma}")

        # X = 20
        self.x = 20
        print(f"X asignado: {self.x}")

        # SUMA = SUMA + X
        self.suma = self.suma + self.x
        print(f"SUMA += X: {self.suma}")

        # Y = 40
        self.y = 40
        print(f"Y asignado: {self.y}")

        # X = X + Y^2
        # En Python, la potencia se representa con **
        self.x = self.x + (self.y ** 2)
        print(f"X = X + Y^2: {self.x}")

        # SUMA = SUMA + X/Y
        self.suma = self.suma + (self.x / self.y)
        print(f"SUMA += X/Y: {self.suma}")

        print(f"EL VALOR DE LA SUMA ES: {self.suma}")

if __name__ == "__main__":
    prueba = PruebaEscritorio()
    prueba.ejecutar_algoritmo()