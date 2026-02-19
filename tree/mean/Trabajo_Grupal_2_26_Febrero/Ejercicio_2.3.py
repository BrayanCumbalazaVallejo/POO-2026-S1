"""
Ejercicio 2.3,Página 73: Estado de un objeto (Clase Automóvil)
Este módulo modela un automóvil con encapsulamiento estricto, 
enumeraciones para sus propiedades y métodos para alterar su estado (velocidad).
"""

from enum import Enum

# --- ENUMERACIONES ---
class tipoCom(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class tipoA(Enum):
    CIUDAD = "Carro de Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class tipoColor(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

# --- CLASE PRINCIPAL ---
class Automovil:
    """Clase que representa un automóvil con todos sus atributos privados (encapsulamiento)."""

    def __init__(self, marca: str, modelo: int, motor: int, tipoCombustible: tipoCom, 
                 tipoAutomovil: tipoA, numeroPuertas: int, cantidadAsientos: int, 
                 velocidadMaxima: int, color: tipoColor):
        """
        Constructor que inicializa los atributos. 
        Nota: La velocidadActual se inicializa en 0 por defecto.
        """
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = motor
        self.__tipoCombustible = tipoCombustible
        self.__tipoAutomovil = tipoAutomovil
        self.__numeroPuertas = numeroPuertas
        self.__cantidadAsientos = cantidadAsientos
        self.__velocidadMaxima = velocidadMaxima
        self.__color = color
        self.__velocidadActual = 0  # El vehículo inicia detenido

    # --- MÉTODOS GET ---
    def getMarca(self) -> str:
        return self.__marca

    def getModelo(self) -> int:
        return self.__modelo

    def getMotor(self) -> int:
        return self.__motor

    def getTipoCombustible(self) -> tipoCom:
        return self.__tipoCombustible

    def getTipoAutomovil(self) -> tipoA:
        return self.__tipoAutomovil

    def getNumeroPuertas(self) -> int:
        return self.__numeroPuertas

    def getCantidadAsientos(self) -> int:
        return self.__cantidadAsientos

    def getVelocidadMaxima(self) -> int:
        return self.__velocidadMaxima

    def getColor(self) -> tipoColor:
        return self.__color

    def getVelocidadActual(self) -> int:
        return self.__velocidadActual

    # --- MÉTODOS SET ---
    def setMarca(self, marca: str):
        self.__marca = marca

    def setModelo(self, modelo: int):
        self.__modelo = modelo

    def setMotor(self, motor: int):
        self.__motor = motor

    def setTipoCombustible(self, tipoCombustible: tipoCom):
        self.__tipoCombustible = tipoCombustible

    def setTipoAutomovil(self, tipoAutomovil: tipoA):
        self.__tipoAutomovil = tipoAutomovil

    def setNumeroPuertas(self, numeroPuertas: int):
        self.__numeroPuertas = numeroPuertas

    def setCantidadAsientos(self, cantidadAsientos: int):
        self.__cantidadAsientos = cantidadAsientos

    def setVelocidadMaxima(self, velocidadMaxima: int):
        self.__velocidadMaxima = velocidadMaxima

    def setColor(self, color: tipoColor):
        self.__color = color

    def setVelocidadActual(self, velocidadActual: int):
        self.__velocidadActual = velocidadActual

    # --- MÉTODOS DE ACCIÓN ---
    def acelerar(self, incrementoVelocidad: int):
        """Aumenta la velocidad si no supera la máxima permitida."""
        if self.__velocidadActual + incrementoVelocidad > self.__velocidadMaxima:
            print(f"Error: No se puede acelerar a {self.__velocidadActual + incrementoVelocidad} km/h porque supera la velocidad máxima de {self.__velocidadMaxima} km/h.")
        else:
            self.__velocidadActual += incrementoVelocidad

    def desacelerar(self, decrementoVelocidad: int):
        """Disminuye la velocidad asegurando que no sea negativa."""
        if self.__velocidadActual - decrementoVelocidad < 0:
            print("Error: No se puede desacelerar a una velocidad negativa.")
        else:
            self.__velocidadActual -= decrementoVelocidad

    def frenar(self):
        """Detiene el vehículo por completo."""
        self.__velocidadActual = 0

    def calcularTiempoLlegada(self, distancia: int) -> float:
        """
        Calcula el tiempo estimado (t = d / v). 
        Evita división por cero si el auto está detenido.
        """
        if self.__velocidadActual == 0:
            print("El automóvil está detenido. Tiempo de llegada infinito.")
            return 0.0
        return distancia / self.__velocidadActual

    def imprimir(self):
        """Muestra por pantalla todos los atributos del automóvil."""
        print("\n--- Atributos del Automóvil ---")
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Motor: {self.__motor} L")
        print(f"Tipo de Combustible: {self.__tipoCombustible.value}")
        print(f"Tipo de Automóvil: {self.__tipoAutomovil.value}")
        print(f"Número de Puertas: {self.__numeroPuertas}")
        print(f"Cantidad de Asientos: {self.__cantidadAsientos}")
        print(f"Velocidad Máxima: {self.__velocidadMaxima} km/h")
        print(f"Color: {self.__color.value}")
        print(f"Velocidad Actual: {self.__velocidadActual} km/h")
        print("-------------------------------")


# --- MÉTODO MAIN ---
if __name__ == "__main__":
    # 1. Crear un automóvil
    mi_auto = Automovil("Toyota", 2026, 2000, tipoCom.GASOLINA, tipoA.SUV, 5, 5, 180, tipoColor.NEGRO)
    
    # Mostrar estado inicial
    mi_auto.imprimir()

    # 2. Colocar su velocidad actual en 100 km/h
    print("\n--- Iniciando simulación de velocidad ---")
    mi_auto.setVelocidadActual(100)
    print(f"Velocidad tras establecer a 100 km/h: {mi_auto.getVelocidadActual()} km/h")

    # 3. Aumentar su velocidad en 20 km/h
    mi_auto.acelerar(20)
    print(f"Velocidad tras acelerar 20 km/h: {mi_auto.getVelocidadActual()} km/h")

    # 4. Decrementar su velocidad en 50 km/h
    mi_auto.desacelerar(50)
    print(f"Velocidad tras desacelerar 50 km/h: {mi_auto.getVelocidadActual()} km/h")

    # 5. Frenar
    mi_auto.frenar()
    print(f"Velocidad tras frenar: {mi_auto.getVelocidadActual()} km/h")