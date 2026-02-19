"""
Ejercicio 2.5, Página 95:: Definición de métodos con parámetros
Este módulo modela una Cuenta Bancaria y permite realizar operaciones 
básicas como consignar, retirar, transferir a otras cuentas y comparar titulares.
"""

from enum import Enum

class tipoCuenta(Enum):
    """Enumeración para los tipos de cuenta bancaria."""
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    """Clase que representa una cuenta bancaria y sus operaciones operativas."""

    def __init__(self, nombresTitular: str, apellidosTitular: str, numeroCuenta: int, tipo: tipoCuenta):
        """
        Constructor que inicializa los atributos. 
        El saldo inicial siempre comienza en 0 según el requerimiento.
        """
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipo = tipo
        self.saldo = 0.0  # El saldo inicia en cero

    def imprimir(self):
        """Imprime por pantalla los valores de los atributos de la cuenta."""
        print(f"\n--- Detalles de la Cuenta: {self.numeroCuenta} ---")
        print(f"Titular: {self.nombresTitular} {self.apellidosTitular}")
        print(f"Tipo de cuenta: {self.tipo.value}")
        print(f"Saldo actual: ${self.saldo:.2f}")
        print("-" * 35)

    def consultarSaldo(self):
        """Consulta e imprime el saldo actual de la cuenta."""
        print(f"El saldo de la cuenta {self.numeroCuenta} es: ${self.saldo:.2f}")

    def consignar(self, valor: int) -> bool:
        """
        Consigna un valor en la cuenta.
        Retorna True si la operación es exitosa (valor positivo).
        """
        if valor > 0:
            self.saldo += valor
            print(f"Se han consignado ${valor} a la cuenta {self.numeroCuenta}.")
            return True
        else:
            print("Error: El valor a consignar debe ser mayor a cero.")
            return False

    def retirar(self, valor: int) -> bool:
        """
        Retira un valor de la cuenta si hay fondos suficientes.
        Retorna True si el retiro es exitoso, False en caso contrario.
        """
        if valor <= 0:
            print("Error: El valor a retirar debe ser mayor a cero.")
            return False
        
        if valor > self.saldo:
            print(f"Error: Fondos insuficientes. Intenta retirar ${valor} pero su saldo es ${self.saldo}.")
            return False
        else:
            self.saldo -= valor
            print(f"Se han retirado ${valor} de la cuenta {self.numeroCuenta}.")
            return True

    def compararCuentas(self, cuenta: 'CuentaBancaria'):
        """
        Compara si la cuenta actual y la cuenta pasada por parámetro 
        pertenecen al mismo titular (mismos nombres y apellidos).
        """
        if (self.nombresTitular.lower() == cuenta.nombresTitular.lower() and 
            self.apellidosTitular.lower() == cuenta.apellidosTitular.lower()):
            print(f"Las cuentas {self.numeroCuenta} y {cuenta.numeroCuenta} pertenecen al mismo titular: {self.nombresTitular} {self.apellidosTitular}.")
        else:
            print(f"Las cuentas {self.numeroCuenta} y {cuenta.numeroCuenta} pertenecen a titulares diferentes.")

    def transferencia(self, cuenta: 'CuentaBancaria', valor: int):
        """
        Realiza una transferencia de la cuenta actual a otra cuenta.
        Utiliza los métodos retirar y consignar para asegurar la lógica de fondos.
        """
        print(f"\n[ Iniciando transferencia de ${valor} de Cuenta {self.numeroCuenta} a Cuenta {cuenta.numeroCuenta} ]")
        # Si se logra retirar el dinero de esta cuenta...
        if self.retirar(valor):
            # ...se consigna en la cuenta destino
            cuenta.consignar(valor)
            print("Transferencia completada con éxito.")
        else:
            print("Transferencia fallida debido a fondos insuficientes.")


# --- MÉTODO MAIN ---
if __name__ == "__main__":
    # 1. Crear dos cuentas bancarias
    cuenta1 = CuentaBancaria("Brayan", "Cumbalaza", 1001, tipoCuenta.AHORROS)
    cuenta2 = CuentaBancaria("Daniel", "Maldonado", 1002, tipoCuenta.CORRIENTE)
    cuenta3 = CuentaBancaria("Brayan", "Cumbalaza", 1003, tipoCuenta.CORRIENTE) # Otra cuenta para Brayan

    # Mostrar estado inicial
    cuenta1.imprimir()
    cuenta2.imprimir()

    # 2. Probar consignar y consultar saldo
    print("\n--- Pruebas de Consignación ---")
    cuenta1.consignar(50000)
    cuenta2.consignar(100000)
    cuenta1.consultarSaldo()

    # 3. Probar retiro (exitoso y fallido)
    print("\n--- Pruebas de Retiro ---")
    cuenta1.retirar(20000)   # Exitoso
    cuenta1.retirar(100000)  # Fallido (fondos insuficientes)

    # 4. Probar transferencia
    cuenta2.transferencia(cuenta1, 30000)
    
    # Consultar saldos tras la transferencia
    print("\n--- Saldos después de la transferencia ---")
    cuenta1.consultarSaldo()
    cuenta2.consultarSaldo()

    # 5. Probar comparación de cuentas
    print("\n--- Prueba de Comparación de Cuentas ---")
    cuenta1.compararCuentas(cuenta2) # Diferentes titulares
    cuenta1.compararCuentas(cuenta3) # Mismo titular