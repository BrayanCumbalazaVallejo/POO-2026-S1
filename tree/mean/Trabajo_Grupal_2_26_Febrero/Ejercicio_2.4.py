"""
Ejercicio 2.4, Página 86: Clases sobre figuras geométricas
Lenguaje: Python
"""

import math

# ---------------------------------------------------------
# ENUNCIADO: Clases sobre figuras geométricas
# ---------------------------------------------------------
# Se requiere un programa que modele varias figuras geométricas: el círculo,
# el rectángulo, el cuadrado y el triángulo rectángulo.
#
# Atributos:
# - El círculo tiene como atributo su radio en centímetros.
# - El rectángulo, su base y altura en centímetros.
# - El cuadrado, la longitud de sus lados en centímetros.
# - El triángulo, su base y altura en centímetros.
#
# Métodos requeridos:
# - Determinar el área y el perímetro de cada figura geométrica.
# - Para el triángulo rectángulo se requiere además:
#   > Un método que calcule la hipotenusa.
#   > Un método para determinar qué tipo de triángulo es (Equilátero, Isósceles, Escaleno).
#
# Se debe desarrollar una clase de prueba con un método main para crear las
# cuatro figuras y probar los métodos respectivos.

class Circulo:
    """Clase que define un círculo."""
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo: pi * r^2"""
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del círculo: 2 * pi * r"""
        return 2 * math.pi * self.radio


class Rectangulo:
    """Clase que define un rectángulo."""
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo: base * altura"""
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del rectángulo: 2 * (base + altura)"""
        return 2 * (self.base + self.altura)


class Cuadrado:
    """Clase que define un cuadrado."""
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado: lado * lado"""
        return self.lado * self.lado

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del cuadrado: 4 * lado"""
        return 4 * self.lado


class TrianguloRectangulo:
    """Clase que define un triángulo rectángulo."""
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_hipotenusa(self) -> float:
        """
        Calcula la hipotenusa usando el teorema de Pitágoras.
        h = raiz_cuadrada(base^2 + altura^2)
        """
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def calcular_area(self) -> float:
        """Calcula el área del triángulo: (base * altura) / 2"""
        return (self.base * self.altura) / 2

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro: base + altura + hipotenusa"""
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        """
        Determina el tipo de triángulo según la longitud de sus lados:
        - Equilátero: 3 lados iguales.
        - Isósceles: 2 lados iguales.
        - Escaleno: 3 lados diferentes.
        """
        # Obtenemos los tres lados
        a = self.base
        b = self.altura
        c = self.calcular_hipotenusa()

        # Comparaciones (usando una pequeña tolerancia para flotantes si fuera necesario, 
        # pero aquí usamos comparación directa para seguir la lógica estándar)
        if a == b and a == c and b == c:
            print("El triángulo es: Equilátero") 
            # Nota matemática: Un triángulo rectángulo nunca puede ser equilátero, 
            # pero se incluye la lógica por requerimiento del enunciado general.
        elif a == b or a == c or b == c:
            print("El triángulo es: Isósceles")
        else:
            print("El triángulo es: Escaleno")


def main():
    print("--- EJECUCIÓN DEL EJERCICIO 2.4: Figuras Geométricas ---")

    # 1. Prueba del Círculo
    print("\n--- CÍRCULO ---")
    radio_circulo = 2
    figura1 = Circulo(radio_circulo)
    print(f"El radio es: {radio_circulo} cm")
    print(f"El área es: {figura1.calcular_area():.4f} cm²")
    print(f"El perímetro es: {figura1.calcular_perimetro():.4f} cm")

    # 2. Prueba del Rectángulo
    print("\n--- RECTÁNGULO ---")
    base_rect = 10
    altura_rect = 20 # Cambiado a valores numéricos para ejemplo
    figura2 = Rectangulo(base_rect, altura_rect)
    print(f"La base es: {base_rect} cm, La altura es: {altura_rect} cm")
    print(f"El área es: {figura2.calcular_area()} cm²")
    print(f"El perímetro es: {figura2.calcular_perimetro()} cm")

    # 3. Prueba del Cuadrado
    print("\n--- CUADRADO ---")
    lado_cuadrado = 3
    figura3 = Cuadrado(lado_cuadrado)
    print(f"El lado es: {lado_cuadrado} cm")
    print(f"El área es: {figura3.calcular_area()} cm²")
    print(f"El perímetro es: {figura3.calcular_perimetro()} cm")

    # 4. Prueba del Triángulo Rectángulo
    print("\n--- TRIÁNGULO RECTÁNGULO ---")
    base_tri = 3
    altura_tri = 5
    figura4 = TrianguloRectangulo(base_tri, altura_tri)
    print(f"La base es: {base_tri} cm, La altura es: {altura_tri} cm")
    print(f"La hipotenusa es: {figura4.calcular_hipotenusa():.4f} cm")
    print(f"El área es: {figura4.calcular_area()} cm²")
    print(f"El perímetro es: {figura4.calcular_perimetro():.4f} cm")
    figura4.determinar_tipo_triangulo()

if __name__ == "__main__":
    main()