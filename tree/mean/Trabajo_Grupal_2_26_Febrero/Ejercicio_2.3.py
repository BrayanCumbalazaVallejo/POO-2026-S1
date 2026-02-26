"""
Ejercicio 2.3,Página 73: Estado de un objeto (Clase Automóvil)
Este módulo modela un automóvil con encapsulamiento estricto, 
enumeraciones para sus propiedades y métodos para alterar su estado (velocidad).
"""
from enum import Enum

# --- DEFINICIÓN DE ENUMERACIONES ---

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class TipoAutomovil(Enum):
    CARRO_CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

# --- DEFINICIÓN DE LA CLASE ---

class Automovil:
    """
    Clase que modela el concepto de un automóvil con su estado y comportamiento.
    """
    def __init__(self, marca: str, modelo: int, motor: float, tipo_combustible: TipoCombustible, 
                 tipo_automovil: TipoAutomovil, numero_puertas: int, cantidad_asientos: int, 
                 velocidad_maxima: float, color: Color, velocidad_actual: float = 0.0):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual

    # --- MÉTODOS GET Y SET ---
    
    def get_marca(self) -> str: return self.marca
    def set_marca(self, marca: str): self.marca = marca

    def get_modelo(self) -> int: return self.modelo
    def set_modelo(self, modelo: int): self.modelo = modelo

    def get_motor(self) -> float: return self.motor
    def set_motor(self, motor: float): self.motor = motor

    def get_tipo_combustible(self) -> TipoCombustible: return self.tipo_combustible
    def set_tipo_combustible(self, tipo: TipoCombustible): self.tipo_combustible = tipo

    def get_tipo_automovil(self) -> TipoAutomovil: return self.tipo_automovil
    def set_tipo_automovil(self, tipo: TipoAutomovil): self.tipo_automovil = tipo

    def get_numero_puertas(self) -> int: return self.numero_puertas
    def set_numero_puertas(self, puertas: int): self.numero_puertas = puertas

    def get_cantidad_asientos(self) -> int: return self.cantidad_asientos
    def set_cantidad_asientos(self, asientos: int): self.cantidad_asientos = asientos

    def get_velocidad_maxima(self) -> float: return self.velocidad_maxima
    def set_velocidad_maxima(self, vel_max: float): self.velocidad_maxima = vel_max

    def get_color(self) -> Color: return self.color
    def set_color(self, color: Color): self.color = color

    def get_velocidad_actual(self) -> float: return self.velocidad_actual
    def set_velocidad_actual(self, vel_actual: float): 
        if vel_actual <= self.velocidad_maxima:
            self.velocidad_actual = vel_actual
        else:
            print("Error: La velocidad asignada supera la máxima permitida.")

    # --- MÉTODOS DE COMPORTAMIENTO ---

    def acelerar(self, incremento: float):
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
            print(f"Acelerando... Nueva velocidad: {self.velocidad_actual} km/h")
        else:
            print(f"No se puede acelerar {incremento} km/h. Se superaría la velocidad máxima de {self.velocidad_maxima} km/h.")

    def desacelerar(self, decremento: float):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
            print(f"Desacelerando... Nueva velocidad: {self.velocidad_actual} km/h")
        else:
            print(f"No se puede desacelerar {decremento} km/h. La velocidad no puede ser negativa.")

    def frenar(self):
        self.velocidad_actual = 0
        print("Frenando... El vehículo se ha detenido. Velocidad: 0 km/h")

    def calcular_tiempo_llegada(self, distancia: float) -> float:
        if self.velocidad_actual == 0:
            print("El vehículo está detenido. El tiempo de llegada es infinito.")
            return -1.0
        tiempo = distancia / self.velocidad_actual
        return tiempo

    def mostrar_atributos(self):
        print("\n=== ATRIBUTOS DEL AUTOMÓVIL ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Combustible: {self.tipo_combustible.value}")
        print(f"Tipo: {self.tipo_automovil.value}")
        print(f"Puertas: {self.numero_puertas}")
        print(f"Asientos: {self.cantidad_asientos}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value}")
        print(f"Velocidad Actual: {self.velocidad_actual} km/h")
        print("===============================\n")

# --- FUNCIÓN PRINCIPAL ---

def main():
    print("=== REGISTRO DE AUTOMÓVIL ===")
    
    # Captura de datos básicos por teclado
    marca = input("Ingrese la marca del automóvil: ")
    
    while True:
        try:
            modelo = int(input("Ingrese el modelo (año): "))
            motor = float(input("Ingrese el cilindraje del motor (ej. 1.6): "))
            puertas = int(input("Número de puertas: "))
            asientos = int(input("Cantidad de asientos: "))
            vel_maxima = float(input("Velocidad máxima (km/h): "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    # Para simplificar la captura en consola, asignamos Enums directamente en este ejemplo,
    # aunque en un sistema real se pediría elegir de un menú como en el ejercicio anterior.
    print("\nConfigurando valores enumerados por defecto para el ejemplo (Gasolina, SUV, Negro)...")
    combustible = TipoCombustible.GASOLINA
    tipo_auto = TipoAutomovil.SUV
    color = Color.NEGRO

    # 1. Crear un automóvil
    mi_auto = Automovil(marca, modelo, motor, combustible, tipo_auto, puertas, asientos, vel_maxima, color)
    
    # Mostrar los atributos iniciales
    mi_auto.mostrar_atributos()

    print("=== PRUEBA DE CONDUCCIÓN ===")
    # 2. Colocar su velocidad actual en 100 km/h
    print("Estableciendo velocidad a 100 km/h...")
    mi_auto.set_velocidad_actual(100.0)
    print(f"Velocidad actual: {mi_auto.get_velocidad_actual()} km/h")

    # 3. Aumentar su velocidad en 20 km/h
    mi_auto.acelerar(20.0)

    # 4. Decrementar su velocidad en 50 km/h
    mi_auto.desacelerar(50.0)

    # 5. Frenar
    mi_auto.frenar()

if __name__ == "__main__":
    main()