import tkinter as tk
from tkinter import messagebox
import math

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class Notas:
    """Clase encargada de realizar los cálculos matemáticos de las notas."""
    def __init__(self, lista_notas):
        self.notas = lista_notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def calcular_desviacion_estandar(self):
        promedio = self.calcular_promedio()
        # Varianza poblacional: suma de (nota - promedio)^2 / N
        varianza = sum(math.pow(nota - promedio, 2) for nota in self.notas) / len(self.notas)
        # Retorna la raíz cuadrada de la varianza
        return math.sqrt(varianza)

    def calcular_mayor(self):
        return max(self.notas)

    def calcular_menor(self):
        return min(self.notas)

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaNotas(tk.Tk):
    """Clase que representa la ventana principal, equivalente a JFrame en Java."""
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana (setTitle, setSize, setResizable)
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        
        # Lista para guardar las referencias de los JTextField (Entry en Python)
        self.entradas_notas = []
        
        # Inicializar los componentes
        self._crear_componentes()
        
        # Centrar la ventana en la pantalla (equivalente a setLocationRelativeTo(null))
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        # Crear los Labels (JLabel) y Entries (JTextField) para las 5 notas
        # Usamos place() que es el equivalente directo de setBounds() en Java
        for i in range(5):
            lbl = tk.Label(self, text=f"Nota {i+1}:", anchor="w")
            lbl.place(x=20, y=20 + (i * 30), width=60, height=25)
            
            txt_entry = tk.Entry(self)
            txt_entry.place(x=100, y=20 + (i * 30), width=150, height=25)
            self.entradas_notas.append(txt_entry)

        # Botón para calcular (JButton)
        btn_calcular = tk.Button(self, text="Calcular", command=self.action_calcular)
        btn_calcular.place(x=20, y=180, width=110, height=30)
        
        # Botón para limpiar los campos
        btn_limpiar = tk.Button(self, text="Limpiar", command=self.action_limpiar)
        btn_limpiar.place(x=140, y=180, width=110, height=30)

        # Labels para mostrar los resultados en la parte inferior
        self.lbl_promedio = tk.Label(self, text="Promedio: ", anchor="w")
        self.lbl_promedio.place(x=20, y=230, width=240, height=25)
        
        self.lbl_desviacion = tk.Label(self, text="Desviación estándar: ", anchor="w")
        self.lbl_desviacion.place(x=20, y=260, width=240, height=25)
        
        self.lbl_mayor = tk.Label(self, text="Mayor nota: ", anchor="w")
        self.lbl_mayor.place(x=20, y=290, width=240, height=25)
        
        self.lbl_menor = tk.Label(self, text="Menor nota: ", anchor="w")
        self.lbl_menor.place(x=20, y=320, width=240, height=25)

    def action_calcular(self):
        """Método equivalente al actionPerformed() para el botón Calcular"""
        try:
            # Extraer el texto de cada Entry y convertirlo a float
            valores = []
            for entry in self.entradas_notas:
                texto = entry.get()
                valores.append(float(texto))
                
            # Instanciar nuestro objeto de la clase Notas
            calculadora = Notas(valores)
            
            # Actualizar los Labels con los resultados formateados a 2 decimales
            self.lbl_promedio.config(text=f"Promedio: {calculadora.calcular_promedio():.2f}")
            self.lbl_desviacion.config(text=f"Desviación estándar: {calculadora.calcular_desviacion_estandar():.2f}")
            self.lbl_mayor.config(text=f"Mayor nota: {calculadora.calcular_mayor():.2f}")
            self.lbl_menor.config(text=f"Menor nota: {calculadora.calcular_menor():.2f}")
            
        except ValueError:
            # Si el usuario ingresa letras o deja campos vacíos, mostramos error
            messagebox.showerror("Error de Entrada", "Por favor, ingrese valores numéricos válidos en las 5 notas.")

    def action_limpiar(self):
        """Limpia los campos y restablece los resultados."""
        for entry in self.entradas_notas:
            entry.delete(0, tk.END)
            
        self.lbl_promedio.config(text="Promedio: ")
        self.lbl_desviacion.config(text="Desviación estándar: ")
        self.lbl_mayor.config(text="Mayor nota: ")
        self.lbl_menor.config(text="Menor nota: ")

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    # Creamos la instancia de la ventana y ejecutamos el ciclo principal
    app = VentanaNotas()
    app.mainloop()