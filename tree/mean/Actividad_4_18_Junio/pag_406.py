"""
Ejercicio Página 406: Clase Vendedor
Este módulo implementa una interfaz gráfica para capturar los datos 
de un vendedor, validando que su edad cumpla con los requisitos 
mediante el manejo de excepciones (ValueError).
"""
import tkinter as tk
from tkinter import messagebox

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class Vendedor:
    """Clase que representa a un Vendedor con validación de edad."""
    
    def __init__(self, nombre, apellidos, edad):
        # Primero verificamos la edad antes de instanciar formalmente los atributos
        self.verificar_edad(edad)
        
        # Si no se lanzaron excepciones, se inicializan los atributos
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def verificar_edad(self, edad):
        """Valida la edad y lanza ValueError (equivalente a IllegalArgumentException)."""
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")

    def imprimir(self):
        """Retorna una cadena con los datos del vendedor."""
        return f"--- Datos del Vendedor ---\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad} años"

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaVendedor(tk.Tk):
    """Interfaz gráfica para capturar e imprimir los datos del Vendedor."""
    
    def __init__(self):
        super().__init__()
        
        self.title("Registro de Vendedor")
        self.geometry("320x350")
        self.resizable(False, False)
        
        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        # Etiquetas y campos de texto (Entry)
        tk.Label(self, text="Nombre:").place(x=30, y=30)
        self.txt_nombre = tk.Entry(self)
        self.txt_nombre.place(x=100, y=30, width=180)

        tk.Label(self, text="Apellidos:").place(x=30, y=70)
        self.txt_apellidos = tk.Entry(self)
        self.txt_apellidos.place(x=100, y=70, width=180)

        tk.Label(self, text="Edad:").place(x=30, y=110)
        self.txt_edad = tk.Entry(self)
        self.txt_edad.place(x=100, y=110, width=80)

        # Botones
        btn_registrar = tk.Button(self, text="Registrar Vendedor", command=self.action_registrar)
        btn_registrar.place(x=30, y=160, width=120, height=30)

        btn_limpiar = tk.Button(self, text="Limpiar", command=self.action_limpiar)
        btn_limpiar.place(x=160, y=160, width=120, height=30)

        # Área de texto para mostrar el resultado (Imprimir)
        self.txt_resultado = tk.Text(self, state=tk.DISABLED, bg="#f5f5f5", font=("Consolas", 10))
        self.txt_resultado.place(x=30, y=210, width=250, height=100)

    def action_registrar(self):
        """Captura los datos, intenta crear el Vendedor y maneja excepciones."""
        nombre = self.txt_nombre.get().strip()
        apellidos = self.txt_apellidos.get().strip()
        edad_str = self.txt_edad.get().strip()

        # Validación básica de campos vacíos
        if not nombre or not apellidos or not edad_str:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        try:
            # Convertimos la edad a entero. Esto puede lanzar ValueError si ingresan letras.
            edad_int = int(edad_str)
            
            # Intentamos instanciar el objeto Vendedor
            # Aquí se invocará verificar_edad() automáticamente
            vendedor = Vendedor(nombre, apellidos, edad_int)
            
            # Si llegamos aquí, la validación fue exitosa. Mostramos los datos.
            self.mostrar_resultado(vendedor.imprimir())
            messagebox.showinfo("Éxito", "Vendedor instanciado correctamente.")

        except ValueError as e:
            # Capturamos tanto el error de int() como las excepciones de nuestra clase
            mensaje_error = str(e)
            # Si el error es por intentar convertir letras a número:
            if "invalid literal" in mensaje_error:
                mensaje_error = "La edad debe ser un valor numérico entero."
            
            messagebox.showerror("Error de Validación", mensaje_error)
            self.mostrar_resultado("Error: No se pudo instanciar el vendedor.")

    def mostrar_resultado(self, texto):
        """Habilita el Text, inserta el mensaje y lo vuelve a deshabilitar."""
        self.txt_resultado.config(state=tk.NORMAL)
        self.txt_resultado.delete(1.0, tk.END)
        self.txt_resultado.insert(tk.END, texto)
        self.txt_resultado.config(state=tk.DISABLED)

    def action_limpiar(self):
        """Limpia todos los campos de la interfaz."""
        self.txt_nombre.delete(0, tk.END)
        self.txt_apellidos.delete(0, tk.END)
        self.txt_edad.delete(0, tk.END)
        self.mostrar_resultado("")

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    app = VentanaVendedor()
    app.mainloop()