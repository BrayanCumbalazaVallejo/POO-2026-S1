"""
Ejercicio 2.4,Página 86: Clases sobre figuras geométricas
Este módulo modela un Círculo, un Rectángulo, un Cuadrado y un Triángulo Rectángulo,
y calcula sus respectivas áreas y perímetros.
"""

import math

class Circulo:
    """Modela un círculo geométrico."""
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo:
    """Modela un rectángulo geométrico."""
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado:
    """Modela un cuadrado geométrico."""
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo:
    """Modela un triángulo rectángulo."""
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        # Teorema de Pitágoras: c = raíz(a^2 + b^2)
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:
        """
        Determina si el triángulo es Equilátero, Isósceles o Escaleno
        basándose en las longitudes de sus tres lados.
        """
        hipotenusa = self.calcular_hipotenusa()
        
        # Redondeamos ligeramente para evitar problemas de precisión con los flotantes
        lados = [round(self.base, 4), round(self.altura, 4), round(hipotenusa, 4)]
        lados_unicos = len(set(lados))
        
        if lados_unicos == 1:
            return "Equilátero" # (Nota matemática: Un triángulo rectángulo real no puede ser equilátero)
        elif lados_unicos == 2:
            return "Isósceles"
        else:
            return "Escaleno"

# --- FUNCIÓN PRINCIPAL ---

def main():
    print("=== SISTEMA DE CÁLCULO DE FIGURAS GEOMÉTRICAS ===")
    
    # Captura de datos para el Círculo
    print("\n--- Datos del Círculo ---")
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo (en cm): "))
            circulo = Circulo(radio)
            break
        except ValueError:
            print("Error: Ingrese un valor numérico.")

    # Captura de datos para el Rectángulo
    print("\n--- Datos del Rectángulo ---")
    while True:
        try:
            base_rect = float(input("Ingrese la base del rectángulo (en cm): "))
            altura_rect = float(input("Ingrese la altura del rectángulo (en cm): "))
            rectangulo = Rectangulo(base_rect, altura_rect)
            break
        except ValueError:
            print("Error: Ingrese valores numéricos.")

    # Captura de datos para el Cuadrado
    print("\n--- Datos del Cuadrado ---")
    while True:
        try:
            lado_cuad = float(input("Ingrese el lado del cuadrado (en cm): "))
            cuadrado = Cuadrado(lado_cuad)
            break
        except ValueError:
            print("Error: Ingrese un valor numérico.")

    # Captura de datos para el Triángulo Rectángulo
    print("\n--- Datos del Triángulo Rectángulo ---")
    while True:
        try:
            base_tri = float(input("Ingrese la base del triángulo (en cm): "))
            altura_tri = float(input("Ingrese la altura del triángulo (en cm): "))
            triangulo = TrianguloRectangulo(base_tri, altura_tri)
            break
        except ValueError:
            print("Error: Ingrese valores numéricos.")

    # Mostrar Resultados
    print("\n" + "="*45)
    print("             RESULTADOS FINALES")
    print("="*45)

    print(f"\n[CÍRCULO] Área: {circulo.calcular_area():.2f} cm² | Perímetro: {circulo.calcular_perimetro():.2f} cm")
    print(f"[RECTÁNGULO] Área: {rectangulo.calcular_area():.2f} cm² | Perímetro: {rectangulo.calcular_perimetro():.2f} cm")
    print(f"[CUADRADO] Área: {cuadrado.calcular_area():.2f} cm² | Perímetro: {cuadrado.calcular_perimetro():.2f} cm")
    
    print("\n[TRIÁNGULO RECTÁNGULO]")
    print(f"  - Área: {triangulo.calcular_area():.2f} cm²")
    print(f"  - Perímetro: {triangulo.calcular_perimetro():.2f} cm")
    print(f"  - Hipotenusa: {triangulo.calcular_hipotenusa():.2f} cm")
    print(f"  - Tipo de Triángulo: {triangulo.determinar_tipo_triangulo()}")
    print("="*45)

if __name__ == "__main__":
    main()