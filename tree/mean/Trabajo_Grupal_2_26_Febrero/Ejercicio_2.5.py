"""
Ejercicio 2.5, Página 95:: Definición de métodos con parámetros
Este módulo modela una Cuenta Bancaria y permite realizar operaciones 
básicas como consignar, retirar, transferir a otras cuentas y comparar titulares.
"""

from enum import Enum

class TipoCuenta(Enum):
    """Enumeración para los tipos de cuenta bancaria."""
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    """Modela una cuenta bancaria con operaciones básicas."""
    
    def __init__(self, nombres: str, apellidos: str, numero_cuenta: str, tipo_cuenta: TipoCuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        # El saldo inicial siempre es cero según el enunciado
        self.saldo = 0.0

    def imprimir_atributos(self):
        """Imprime por pantalla los valores de los atributos de la cuenta."""
        print("\n=== DATOS DE LA CUENTA BANCARIA ===")
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Número de Cuenta: {self.numero_cuenta}")
        print(f"Tipo de Cuenta: {self.tipo_cuenta.value}")
        print(f"Saldo Actual: ${self.saldo:.2f}")
        print("===================================")

    def consultar_saldo(self) -> float:
        """Devuelve el saldo actual de la cuenta."""
        return self.saldo

    def consignar(self, valor: float):
        """Consigna un valor en la cuenta actualizando el saldo."""
        if valor > 0:
            self.saldo += valor
            print(f"Consignación exitosa. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Error: El valor a consignar debe ser mayor a cero.")

    def retirar(self, valor: float):
        """
        Retira un valor de la cuenta si hay fondos suficientes.
        Actualiza el saldo correspondiente.
        """
        if valor <= 0:
            print("Error: El valor a retirar debe ser mayor a cero.")
        elif valor > self.saldo:
            print(f"Error: Fondos insuficientes. Su saldo actual es de ${self.saldo:.2f} y usted intentó retirar ${valor:.2f}.")
        else:
            self.saldo -= valor
            print(f"Retiro exitoso de ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")


def main():
    print("=== APERTURA DE CUENTA BANCARIA ===")
    
    # Captura de datos iniciales
    nombres = input("Ingrese los nombres del titular: ")
    apellidos = input("Ingrese los apellidos del titular: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    
    print("\nSeleccione el tipo de cuenta:")
    print("1. Ahorros")
    print("2. Corriente")
    while True:
        opcion_tipo = input("Opción (1-2): ")
        if opcion_tipo == '1':
            tipo_cuenta = TipoCuenta.AHORROS
            break
        elif opcion_tipo == '2':
            tipo_cuenta = TipoCuenta.CORRIENTE
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    # Creación del objeto CuentaBancaria
    cuenta = CuentaBancaria(nombres, apellidos, numero_cuenta, tipo_cuenta)
    print("\n¡Cuenta creada con éxito! Saldo inicial: $0.00")

    # Menú interactivo para probar los métodos
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Consultar saldo")
        print("2. Consignar dinero")
        print("3. Retirar dinero")
        print("4. Ver datos de la cuenta")
        print("5. Salir")
        
        opcion = input("Seleccione una operación (1-5): ")
        
        if opcion == '1':
            print(f"\nSu saldo actual es: ${cuenta.consultar_saldo():.2f}")
            
        elif opcion == '2':
            try:
                valor = float(input("\nIngrese el valor a consignar: $"))
                cuenta.consignar(valor)
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
                
        elif opcion == '3':
            try:
                valor = float(input("\nIngrese el valor a retirar: $"))
                cuenta.retirar(valor)
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
                
        elif opcion == '4':
            cuenta.imprimir_atributos()
            
        elif opcion == '5':
            print("\nGracias por usar nuestro sistema bancario. ¡Hasta luego!")
            break
            
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()