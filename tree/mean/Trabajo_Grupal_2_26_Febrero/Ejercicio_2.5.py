"""
Ejercicio 2.5, Página 95: Definición de métodos con parámetros (Clase CuentaBancaria)
Lenguaje: Python
"""

from enum import Enum

# ---------------------------------------------------------
# ENUNCIADO: Clase CuentaBancaria
# ---------------------------------------------------------
# Se requiere un programa que modele una cuenta bancaria que posee los
# siguientes atributos:
# - Nombres del titular.
# - Apellidos del titular.
# - Número de la cuenta bancaria.
# - Tipo de cuenta: puede ser una cuenta de ahorros o una cuenta corriente.
# - Saldo de la cuenta.
#
# Requerimientos:
# 1. Definir un constructor que inicialice los atributos de la clase.
#    IMPORTANTE: Cuando se crea una cuenta bancaria, su saldo inicial tiene un valor de cero.
# 2. En una determinada cuenta bancaria se puede:
#    - Imprimir por pantalla los valores de los atributos.
#    - Consultar el saldo.
#    - Consignar un determinado valor (actualizando el saldo).
#    - Retirar un determinado valor (actualizando el saldo).
#      > Validar: No se puede retirar si el valor solicitado supera el saldo actual.

class TipoCuenta(Enum):
    """Enumeración para los tipos de cuenta bancaria."""
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    """
    Clase que define una cuenta bancaria con sus operaciones básicas.
    """
    def __init__(self, nombres: str, apellidos: str, numero_cuenta: str, tipo_cuenta: TipoCuenta):
        """
        Constructor de la cuenta bancaria.
        Inicializa los datos del titular y la cuenta.
        El saldo se inicializa automáticamente en 0.0.
        """
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0  # Requerimiento: saldo inicial cero

    def imprimir_datos(self):
        """Imprime los atributos de la cuenta bancaria."""
        print(f"\n--- Información de la Cuenta ---")
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta.value}")
        print(f"Saldo actual: ${self.saldo:.2f}")

    def consultar_saldo(self) -> float:
        """Retorna el saldo actual de la cuenta."""
        return self.saldo

    def consignar(self, valor: float):
        """
        Consigna (deposita) un valor en la cuenta.
        :param valor: Cantidad monetaria a depositar (debe ser positiva).
        """
        if valor > 0:
            self.saldo += valor
            print(f"Consignación exitosa de ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("El valor a consignar debe ser mayor a cero.")

    def retirar(self, valor: float):
        """
        Retira un valor de la cuenta si hay fondos suficientes.
        :param valor: Cantidad monetaria a retirar.
        """
        if valor <= 0:
            print("El valor a retirar debe ser positivo.")
            return

        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Retiro exitoso de ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print(f"Error: Fondos insuficientes para retirar ${valor:.2f}. Saldo actual: ${self.saldo:.2f}")

def main():
    print("--- EJECUCIÓN DEL EJERCICIO 2.5: Cuenta Bancaria ---")

    # 1. Crear una cuenta bancaria
    cuenta = CuentaBancaria(
        nombres="Pedro",
        apellidos="Pérez",
        numero_cuenta="123456789",
        tipo_cuenta=TipoCuenta.AHORROS
    )

    # 2. Imprimir estado inicial (Saldo debe ser 0)
    cuenta.imprimir_datos()

    # 3. Consignar dinero
    print("\n--- Realizando consignación ---")
    cuenta.consignar(200000) # Consignar 200,000
    
    # 4. Consultar saldo
    print(f"Saldo consultado: ${cuenta.consultar_saldo():.2f}")

    # 5. Retirar dinero (Caso Exitoso)
    print("\n--- Realizando retiro válido ---")
    cuenta.retirar(50000) # Retirar 50,000

    # 6. Retirar dinero (Caso Fondos Insuficientes)
    print("\n--- Intentando retiro inválido (supera saldo) ---")
    cuenta.retirar(300000) # Intentar retirar 300,000 (Saldo restante es 150,000)

    # 7. Estado final
    cuenta.imprimir_datos()

if __name__ == "__main__":
    main()