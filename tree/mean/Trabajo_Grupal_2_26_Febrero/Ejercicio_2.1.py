"""
Ejercicio 2.1: Página 63: Definición de clases (Clase Persona)
Este módulo modela el concepto de una persona con sus atributos básicos
y permite imprimir su información en pantalla.
"""
class Persona:
    """
    Clase que modela el concepto de una persona.
    """
    def __init__(self, nombre: str, apellido: str, numero_documento: str, ano_nacimiento: int):
        # El constructor inicializa los valores de los atributos
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.ano_nacimiento = ano_nacimiento

    def imprimir_informacion(self):
        """
        Método para imprimir en pantalla los valores de los atributos del objeto.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Documento de Identidad: {self.numero_documento}")
        print(f"Año de Nacimiento: {self.ano_nacimiento}")
        print("-" * 30)


def main():
    print("=== SISTEMA DE REGISTRO DE PERSONAS ===")
    personas = []

    # Se requiere crear dos personas mediante captura de datos por teclado
    for i in range(1, 3):
        print(f"\n--- Ingrese los datos de la Persona {i} ---")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        numero_documento = input("Número de Documento: ")
        
        # Validación básica para asegurar que el año sea numérico
        while True:
            try:
                ano_nacimiento = int(input("Año de Nacimiento (ej. 1995): "))
                break
            except ValueError:
                print("Error: Por favor, ingrese un año válido (solo números).")
        
        # Instanciamos el objeto Persona y lo agregamos a nuestra lista
        persona_instancia = Persona(nombre, apellido, numero_documento, ano_nacimiento)
        personas.append(persona_instancia)

    print("\n=== INFORMACIÓN REGISTRADA ===")
    # Recorremos la lista para mostrar la información de las dos personas creadas
    for idx, persona in enumerate(personas, 1):
        print(f"\nMostrando datos de la Persona {idx}:")
        persona.imprimir_informacion()


# Punto de entrada del programa
if __name__ == "__main__":
    main()