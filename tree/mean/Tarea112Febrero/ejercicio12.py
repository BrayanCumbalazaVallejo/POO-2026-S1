"""
Ejercicio Propuesto No 12

Un empleado trabaja 48 horas en la semana a razón de $5.000 hora. El porcentaje de
retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto,
la retención en la fuente y el salario neto del trabajador.
"""

class Empleado:
    """
    Clase que representa a un empleado y calcula su salario
    basado en horas trabajadas y retenciones.
    """
    def __init__(self):
        self.horas_trabajadas = 0
        self.valor_hora = 0
        self.porcentaje_retencion = 0.0
        self.salario_bruto = 0.0
        self.retencion = 0.0
        self.salario_neto = 0.0

    def ingresar_datos(self):
        # Según el enunciado, estos son los datos iniciales
        self.horas_trabajadas = 48
        self.valor_hora = 5000
        self.porcentaje_retencion = 12.5  # Representa el 12.5%

    def calcular_salario(self):
        # Cálculo del salario bruto
        self.salario_bruto = self.horas_trabajadas * self.valor_hora
        
        # Cálculo de la retención en la fuente
        self.retencion = self.salario_bruto * (self.porcentaje_retencion / 100)
        
        # Cálculo del salario neto
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar_info(self):
        print("--- Información Salarial del Trabajador ---")
        print(f"Horas trabajadas en la semana: {self.horas_trabajadas}")
        print(f"Valor por hora: ${self.valor_hora}")
        print(f"Porcentaje de retención: {self.porcentaje_retencion}%")
        print("-" * 41)
        print(f"Salario Bruto:           ${self.salario_bruto:,.2f}")
        print(f"Retención en la fuente:  ${self.retencion:,.2f}")
        print(f"Salario Neto a pagar:    ${self.salario_neto:,.2f}")

if __name__ == "__main__":
    empleado = Empleado()
    empleado.ingresar_datos()
    empleado.calcular_salario()
    empleado.mostrar_info()