"""
Ejercicio 2.4,Página 86: Clases sobre figuras geométricas
Este módulo modela un Círculo, un Rectángulo, un Cuadrado y un Triángulo Rectángulo,
y calcula sus respectivas áreas y perímetros.
"""

import math

class Circulo:
    def __init__(self, radio: int):
        self.radio = radio

    def calcularArea(self) -> float:
        # Área del círculo = pi * radio^2
        return math.pi * math.pow(self.radio, 2)

    def calcularPerimetro(self) -> float:
        # Perímetro del círculo = 2 * pi * radio
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def calcularArea(self) -> float:
        # Área del rectángulo = base * altura
        return self.base * self.altura

    def calcularPerimetro(self) -> float:
        # Perímetro = (2 * base) + (2 * altura)
        return (2 * self.base) + (2 * self.altura)


class Cuadrado:
    def __init__(self, lado: int):
        self.lado = lado

    def calcularArea(self) -> float:
        # Área del cuadrado = lado^2
        return self.lado * self.lado

    def calcularPerimetro(self) -> float:
        # Perímetro = 4 * lado
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def calcularArea(self) -> float:
        # Área del triángulo = (base * altura) / 2
        return (self.base * self.altura) / 2

    def calcularPerimetro(self) -> float:
        # Perímetro = base + altura + hipotenusa
        return self.base + self.altura + self.calcularHipotenusa()

    def calcularHipotenusa(self) -> float:
        # Teorema de Pitágoras: hipotenusa = raíz(base^2 + altura^2)
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def determinarTipoTriangulo(self):
        hipotenusa = self.calcularHipotenusa()
        
        # Condicionales usando el operador lógico 'and' (equivalente a && en Java)
        if (self.base == self.altura) and (self.base == hipotenusa) and (self.altura == hipotenusa):
            print("Es un triángulo equilátero")
        elif (self.base != self.altura) and (self.base != hipotenusa) and (self.altura != hipotenusa):
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


# --- CLASE DE PRUEBA (main) ---
if __name__ == "__main__":
    print("--- Prueba de Figuras Geométricas ---")
    
    # 1. Crear las cuatro figuras con datos de prueba
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)

    # 2. Probar métodos del Círculo
    print("\n[ Círculo ]")
    print(f"Área = {figura1.calcularArea():.2f}")
    print(f"Perímetro = {figura1.calcularPerimetro():.2f}")

    # 3. Probar métodos del Rectángulo
    print("\n[ Rectángulo ]")
    print(f"Área = {figura2.calcularArea():.2f}")
    print(f"Perímetro = {figura2.calcularPerimetro():.2f}")

    # 4. Probar métodos del Cuadrado
    print("\n[ Cuadrado ]")
    print(f"Área = {figura3.calcularArea():.2f}")
    print(f"Perímetro = {figura3.calcularPerimetro():.2f}")

    # 5. Probar métodos del Triángulo Rectángulo
    print("\n[ Triángulo Rectángulo ]")
    print(f"Área = {figura4.calcularArea():.2f}")
    print(f"Perímetro = {figura4.calcularPerimetro():.2f}")
    print(f"Hipotenusa = {figura4.calcularHipotenusa():.2f}")
    figura4.determinarTipoTriangulo()