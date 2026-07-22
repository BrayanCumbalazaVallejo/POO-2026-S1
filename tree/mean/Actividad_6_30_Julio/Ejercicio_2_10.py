"""
Ejercicio 2.10: Sobrecarga de Métodos (Clase Pedido)
Este script implementa la simulación de sobrecarga de métodos en Python
para calcular el costo total de diferentes tipos de pedidos en un restaurante.
"""

class Pedido:
    """
    Nota sobre la sobrecarga en Python:
    Python no soporta la creación de múltiples métodos con el mismo nombre. 
    Para implementar la sobrecarga, se utiliza un único método con 
    parámetros opcionales inicializados en 'None'.
    """
    
    def calcular_pedido(self, primer_plato, bebida, segundo_plato=None, postre=None):
        """
        Calcula el valor del pedido evaluando qué argumentos fueron enviados.
        """
        # Caso 3: Un primer plato, un segundo plato, una bebida y un postre
        if segundo_plato is not None and postre is not None:
            print("=> Procesando: 1er Plato + 2do Plato + Bebida + Postre")
            return primer_plato + segundo_plato + bebida + postre
            
        # Caso 2: Un primer plato, un segundo plato y una bebida
        elif segundo_plato is not None and postre is None:
            print("=> Procesando: 1er Plato + 2do Plato + Bebida")
            return primer_plato + segundo_plato + bebida
            
        # Caso 1: Un primer plato y una bebida
        else:
            print("=> Procesando: 1er Plato + Bebida")
            return primer_plato + bebida


# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (Método main)
# ==========================================
if __name__ == "__main__":
    print("-" * 50)
    print("SISTEMA DE PEDIDOS DEL RESTAURANTE")
    print("-" * 50)
    
    # Instanciamos el objeto de la clase Pedido
    mi_pedido = Pedido()
    
    try:
        # 1. Prueba del primer método (2 parámetros)
        print("\n--- Cliente 1 (1er Plato + Bebida) ---")
        p1 = float(input("Ingrese valor del Primer Plato: $"))
        b1 = float(input("Ingrese valor de la Bebida: $"))
        total_1 = mi_pedido.calcular_pedido(p1, b1)
        print(f"Total a pagar Cliente 1: ${total_1:,.2f}")
        
        # 2. Prueba del segundo método (3 parámetros)
        print("\n--- Cliente 2 (1er Plato + 2do Plato + Bebida) ---")
        p2_1 = float(input("Ingrese valor del Primer Plato: $"))
        p2_2 = float(input("Ingrese valor del Segundo Plato: $"))
        b2 = float(input("Ingrese valor de la Bebida: $"))
        total_2 = mi_pedido.calcular_pedido(p2_1, b2, p2_2)
        print(f"Total a pagar Cliente 2: ${total_2:,.2f}")
        
        # 3. Prueba del tercer método (4 parámetros)
        print("\n--- Cliente 3 (Completo con Postre) ---")
        p3_1 = float(input("Ingrese valor del Primer Plato: $"))
        p3_2 = float(input("Ingrese valor del Segundo Plato: $"))
        b3 = float(input("Ingrese valor de la Bebida: $"))
        postre3 = float(input("Ingrese valor del Postre: $"))
        total_3 = mi_pedido.calcular_pedido(p3_1, b3, p3_2, postre3)
        print(f"Total a pagar Cliente 3: ${total_3:,.2f}")
        
    except ValueError:
        print("\n[Error] Entrada inválida. Por favor, ingrese únicamente valores numéricos.")
        
    print("\n" + "-" * 50)