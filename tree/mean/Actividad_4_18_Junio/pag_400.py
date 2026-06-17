"""
Ejercicio Página 400: PruebaExcepciones
Este módulo implementa una interfaz gráfica para simular la ejecución 
de bloques try-except-finally, mostrando en un área de texto 
los mensajes generados por el manejo de excepciones.
"""
# ==========================================
import tkinter as tk

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class PruebaExcepciones:
    """Clase que ejecuta sentencias que lanzan excepciones y recolecta los logs."""
    
    def ejecutar_pruebas(self):
        """Ejecuta los dos bloques try y devuelve el registro de ejecución."""
        logs = []
        
        # --- Primer bloque try ---
        try:
            logs.append("Ingresando al primer try")
            # En Python, la división por cero lanza ZeroDivisionError
            cociente = 10000 / 0 
            logs.append("Después de la división") # Esta instrucción nunca será ejecutada
        except ZeroDivisionError: # Equivalente a ArithmeticException
            logs.append("División por cero")
        finally:
            # La sentencia finally siempre se ejecuta
            logs.append("Ingresando al primer finally")

        logs.append("-" * 30)

        # --- Segundo bloque try ---
        try:
            logs.append("Ingresando al segundo try")
            objeto = None
            # Forzamos un AttributeError intentando llamar a un método de None
            # (Equivalente al NullPointerException del objeto.toString() en Java)
            objeto.metodo_inexistente() 
            logs.append("Imprimiendo objeto") # Esta instrucción nunca será ejecutada
        except ZeroDivisionError:
            # La excepción lanzada no es de este tipo
            logs.append("División por cero")
        except Exception as e:
            # Se captura la excepción general
            logs.append("Ocurrió una excepción")
        finally:
            # La sentencia finally siempre se ejecuta
            logs.append("Ingresando al segundo finally")

        # Retornamos todo el texto unido por saltos de línea
        return "\n".join(logs)

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaPruebaExcepciones(tk.Tk):
    """Clase que representa la ventana principal de la aplicación."""
    
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana
        self.title("Prueba de Excepciones")
        self.geometry("380x360")
        self.resizable(False, False)
        
        # Inicializar los componentes
        self._crear_componentes()
        
        # Centrar la ventana en la pantalla
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        # Etiqueta de título
        lbl_titulo = tk.Label(self, text="Consola de Ejecución de Excepciones", font=("Arial", 10, "bold"))
        lbl_titulo.place(x=20, y=10, width=340, height=25)

        # Botón para ejecutar la prueba
        btn_ejecutar = tk.Button(self, text="Ejecutar Código", command=self.action_ejecutar)
        btn_ejecutar.place(x=130, y=45, width=120, height=30)

        # Área de texto (Text) equivalente a un JTextArea para mostrar resultados
        self.txt_consola = tk.Text(self, state=tk.DISABLED, bg="#f5f5f5", font=("Consolas", 10))
        self.txt_consola.place(x=20, y=85, width=340, height=250)

    def action_ejecutar(self):
        """Método asociado al botón para ejecutar el código y mostrar resultados."""
        # Instanciar el objeto de la lógica
        prueba = PruebaExcepciones()
        
        # Obtener los logs de la ejecución
        resultado = prueba.ejecutar_pruebas()
        
        # Habilitar el Text, insertar el resultado y volver a deshabilitar (Solo lectura)
        self.txt_consola.config(state=tk.NORMAL)
        self.txt_consola.delete(1.0, tk.END)
        self.txt_consola.insert(tk.END, resultado)
        self.txt_consola.config(state=tk.DISABLED)

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    app = VentanaPruebaExcepciones()
    app.mainloop()