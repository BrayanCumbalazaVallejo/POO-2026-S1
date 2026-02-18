"""
Ejercicio 2.3, Página 73: Estado de un objeto (Clase Automóvil)
Lenguaje: Python
"""

from enum import Enum

# ---------------------------------------------------------
# ENUNCIADO: Clase Automóvil
# ---------------------------------------------------------
# Se requiere un programa que modele el concepto de un automóvil.
#
# Atributos:
# - Marca: nombre del fabricante.
# - Modelo: año de fabricación.
# - Motor: volumen en litros del cilindraje.
# - Tipo de combustible: Enum (gasolina, bioetanol, diésel, biodiésel, gas natural).
# - Tipo de automóvil: Enum (carro de ciudad, subcompacto, compacto, familiar, ejecutivo, SUV).
# - Número de puertas: cantidad de puertas.
# - Cantidad de asientos: número de asientos disponibles.
# - Velocidad máxima: velocidad máxima sostenida en km/h.
# - Color: Enum (blanco, negro, rojo, naranja, amarillo, verde, azul, violeta).
# - Velocidad actual: velocidad del vehículo en un momento dado.
#
# Métodos:
# 1. Constructor con parámetros para los atributos.
# 2. Métodos get y set.
# 3. Acelerar(velocidad): Aumentar velocidad actual sin superar la máxima.
# 4. Desacelerar(velocidad): Disminuir velocidad sin ser negativa.
# 5. Frenar(): Colocar velocidad actual en cero.
# 6. Calcular tiempo estimado de llegada (distancia / velocidad actual).
# 7. Imprimir atributos.
# 8. Main: Crear auto, poner velocidad en 100, aumentar 20, bajar 50, frenar.

# --- Definición de Enumeraciones (Enums) ---

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class TipoAutomovil(Enum):
    CIUDAD = "Carro de Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

# --- Definición de la Clase Automóvil ---

class Automovil:
    """
    Clase que modela un automóvil con sus características y comportamiento.
    """
    def __init__(self, marca: str, modelo: int, motor: float, 
                 tipo_combustible: TipoCombustible, tipo_automovil: TipoAutomovil, 
                 numero_puertas: int, cantidad_asientos: int, 
                 velocidad_maxima: float, color: TipoColor, velocidad_actual: float = 0):
        """
        Constructor de la clase Automovil.
        :param modelo: Año de fabricación (int).
        :param motor: Volumen en litros (float).
        :param velocidad_actual: Inicialmente 0 por defecto.
        """
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima
        self._color = color
        self._velocidad_actual = velocidad_actual

    # --- Métodos Get y Set ---
    
    def get_marca(self): return self._marca
    def set_marca(self, marca): self._marca = marca

    def get_modelo(self): return self._modelo
    def set_modelo(self, modelo): self._modelo = modelo

    def get_motor(self): return self._motor
    def set_motor(self, motor): self._motor = motor

    def get_tipo_combustible(self): return self._tipo_combustible
    def set_tipo_combustible(self, tipo): self._tipo_combustible = tipo

    def get_tipo_automovil(self): return self._tipo_automovil
    def set_tipo_automovil(self, tipo): self._tipo_automovil = tipo

    def get_numero_puertas(self): return self._numero_puertas
    def set_numero_puertas(self, puertas): self._numero_puertas = puertas

    def get_cantidad_asientos(self): return self._cantidad_asientos
    def set_cantidad_asientos(self, asientos): self._cantidad_asientos = asientos

    def get_velocidad_maxima(self): return self._velocidad_maxima
    def set_velocidad_maxima(self, max_vel): self._velocidad_maxima = max_vel

    def get_color(self): return self._color
    def set_color(self, color): self._color = color

    def get_velocidad_actual(self): return self._velocidad_actual
    def set_velocidad_actual(self, velocidad): self._velocidad_actual = velocidad

    # --- Métodos de comportamiento ---

    def acelerar(self, aumento_velocidad: float):
        """
        Incrementa la velocidad actual.
        Si la suma supera la velocidad máxima, no se aplica y se muestra mensaje.
        """
        nueva_velocidad = self._velocidad_actual + aumento_velocidad
        if nueva_velocidad > self._velocidad_maxima:
            print(f"Mensaje: No se puede acelerar a {nueva_velocidad} km/h. "
                  f"Supera la velocidad máxima de {self._velocidad_maxima} km/h.")
        else:
            self._velocidad_actual = nueva_velocidad
            print(f"Acelerando... Nueva velocidad: {self._velocidad_actual} km/h")

    def desacelerar(self, disminucion_velocidad: float):
        """
        Decrementa la velocidad actual.
        Si el resultado es negativo, no se aplica y se muestra mensaje.
        """
        nueva_velocidad = self._velocidad_actual - disminucion_velocidad
        if nueva_velocidad < 0:
            print(f"Mensaje: No se puede desacelerar en {disminucion_velocidad} km/h. "
                  f"La velocidad resultante sería negativa.")
        else:
            self._velocidad_actual = nueva_velocidad
            print(f"Desacelerando... Nueva velocidad: {self._velocidad_actual} km/h")

    def frenar(self):
        """
        Establece la velocidad actual en 0.
        """
        self._velocidad_actual = 0
        print("Frenando... El automóvil se ha detenido (0 km/h).")

    def calcular_tiempo_llegada(self, distancia_km: float) -> float:
        """
        Calcula el tiempo estimado para recorrer una distancia dada.
        Tiempo = Distancia / Velocidad Actual.
        Retorna None si la velocidad es 0 para evitar división por cero.
        """
        if self._velocidad_actual == 0:
            print("El auto está detenido, tiempo de llegada infinito.")
            return None
        return distancia_km / self._velocidad_actual

    def imprimir(self):
        """
        Imprime los atributos del automóvil.
        """
        print("\n--- Datos del Automóvil ---")
        print(f"Marca: {self._marca}")
        print(f"Modelo (Año): {self._modelo}")
        print(f"Motor: {self._motor} Litros")
        print(f"Tipo de Combustible: {self._tipo_combustible.value}")
        print(f"Tipo de Automóvil: {self._tipo_automovil.value}")
        print(f"Número de Puertas: {self._numero_puertas}")
        print(f"Cantidad de Asientos: {self._cantidad_asientos}")
        print(f"Velocidad Máxima: {self._velocidad_maxima} km/h")
        print(f"Color: {self._color.value}")
        print(f"Velocidad Actual: {self._velocidad_actual} km/h")

def main():
    print("--- EJECUCIÓN DEL EJERCICIO 2.3 ---")
    
    # 1. Crear un automóvil
    auto1 = Automovil(
        marca="Ford",
        modelo=2018,
        motor=2.0,
        tipo_combustible=TipoCombustible.GASOLINA,
        tipo_automovil=TipoAutomovil.FAMILIAR,
        numero_puertas=5,
        cantidad_asientos=5,
        velocidad_maxima=250.0,
        color=TipoColor.NEGRO,
        velocidad_actual=0.0
    )
    
    # Imprimir datos iniciales
    auto1.imprimir()

    print("\n--- Probando Cambios de Velocidad ---")
    
    # 2. Colocar su velocidad actual en 100 km/h
    print("\n1. Estableciendo velocidad a 100 km/h")
    auto1.set_velocidad_actual(100)
    print(f"Velocidad actual: {auto1.get_velocidad_actual()} km/h")

    # 3. Aumentar su velocidad en 20 km/h
    print("\n2. Aumentando velocidad en 20 km/h")
    auto1.acelerar(20)

    # 4. Decrementar su velocidad en 50 km/h
    print("\n3. Desacelerando en 50 km/h")
    auto1.desacelerar(50)

    # 5. Frenar
    print("\n4. Frenando el automóvil")
    auto1.frenar()

    # (Extra) Probar límites
    print("\n--- Pruebas extra de validación ---")
    auto1.set_velocidad_actual(240)
    print(f"Velocidad reseteada a: {auto1.get_velocidad_actual()} km/h")
    print("Intentando acelerar 20 km/h (superaría máxima de 250):")
    auto1.acelerar(20)
    
    print("Intentando desacelerar 300 km/h (sería negativo):")
    auto1.desacelerar(300)

if __name__ == "__main__":
    main()