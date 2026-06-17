"""
Ejercicio Página 412: Cálculos Numéricos
Este módulo implementa una interfaz gráfica para calcular el logaritmo neperiano
y la raíz cuadrada de un número, gestionando excepciones matemáticas y de formato.
"""
import tkinter as tk
from tkinter import messagebox
import math

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class CalculosNumericos:
    """Clase que provee métodos estáticos para cálculos matemáticos."""

    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        """Calcula el logaritmo neperiano. Lanza ArithmeticError si no es positivo."""
        if valor <= 0:
            # En Java esto es ArithmeticException. En Python simulamos con ArithmeticError
            raise ArithmeticError("El valor debe ser positivo (> 0) para calcular el logaritmo.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        """Calcula la raíz cuadrada. Lanza ArithmeticError si no es positivo."""
        if valor <= 0:
            raise ArithmeticError("El valor debe ser positivo (> 0) para calcular la raíz cuadrada.")
        return math.sqrt(valor)

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaCalculos(tk.Tk):
    """Interfaz gráfica para interactuar con la clase estática CalculosNumericos."""

    def __init__(self):
        super().__init__()

        self.title("Cálculos Numéricos")
        self.geometry("350x260")
        self.resizable(False, False)

        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        # Etiqueta y campo de texto para el valor
        tk.Label(self, text="Ingrese un valor numérico:").place(x=20, y=20)
        self.txt_valor = tk.Entry(self)
        self.txt_valor.place(x=170, y=20, width=150)

        # Botones de operaciones
        btn_log = tk.Button(self, text="Calcular Logaritmo (ln)", command=self.action_calcular_logaritmo)
        btn_log.place(x=20, y=60, width=150, height=30)

        btn_raiz = tk.Button(self, text="Calcular Raíz Cuadrada", command=self.action_calcular_raiz)
        btn_raiz.place(x=180, y=60, width=140, height=30)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self.action_limpiar)
        btn_limpiar.place(x=100, y=100, width=150, height=30)

        # Área de texto para mostrar resultados
        self.txt_resultado = tk.Text(self, state=tk.DISABLED, bg="#f5f5f5", font=("Consolas", 10))
        self.txt_resultado.place(x=20, y=140, width=310, height=100)

    def obtener_valor(self):
        """Valida la entrada del usuario y retorna el valor en formato float."""
        texto = self.txt_valor.get().strip()
        if not texto:
            raise ValueError("vacío")
        # Intenta convertir a float. Lanza ValueError si ingresan letras
        # Equivalente a InputMismatchException en Java
        return float(texto)

    def action_calcular_logaritmo(self):
        try:
            valor = self.obtener_valor()
            # Llamado al método estático sin instanciar la clase
            resultado = CalculosNumericos.calcular_logaritmo_neperiano(valor)
            self.mostrar_resultado(f"Logaritmo neperiano de {valor}:\n{resultado:.4f}")
            
        except ValueError as e:
            if str(e) == "vacío":
                messagebox.showwarning("Campo vacío", "Por favor, ingrese un número.")
            else:
                messagebox.showerror("Error de Formato", "No ingrese letras. Ingrese un número válido.")
                self.mostrar_resultado("Error: Entrada no válida (InputMismatchException).")
                
        except ArithmeticError as e:
            messagebox.showerror("Error Aritmético", str(e))
            self.mostrar_resultado(f"Error Aritmético:\n{e}")

    def action_calcular_raiz(self):
        try:
            valor = self.obtener_valor()
            # Llamado al método estático sin instanciar la clase
            resultado = CalculosNumericos.calcular_raiz_cuadrada(valor)
            self.mostrar_resultado(f"Raíz cuadrada de {valor}:\n{resultado:.4f}")
            
        except ValueError as e:
            if str(e) == "vacío":
                messagebox.showwarning("Campo vacío", "Por favor, ingrese un número.")
            else:
                messagebox.showerror("Error de Formato", "No ingrese letras. Ingrese un número válido.")
                self.mostrar_resultado("Error: Entrada no válida (InputMismatchException).")
                
        except ArithmeticError as e:
            messagebox.showerror("Error Aritmético", str(e))
            self.mostrar_resultado(f"Error Aritmético:\n{e}")

    def mostrar_resultado(self, texto):
        """Habilita el área de texto, inserta el resultado y la vuelve a bloquear."""
        self.txt_resultado.config(state=tk.NORMAL)
        self.txt_resultado.delete(1.0, tk.END)
        self.txt_resultado.insert(tk.END, texto)
        self.txt_resultado.config(state=tk.DISABLED)

    def action_limpiar(self):
        """Limpia la entrada y el área de resultados."""
        self.txt_valor.delete(0, tk.END)
        self.mostrar_resultado("")

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    app = VentanaCalculos()
    app.mainloop()