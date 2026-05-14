import tkinter as tk
from tkinter import messagebox
import math

# ==========================================
# JERARQUÍA DE CLASES (Lógica del Negocio)
# ==========================================

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Volumen = pi * r^2 * h
        self.volumen = math.pi * (self.radio ** 2) * self.altura

    def calcular_superficie(self):
        # Superficie = 2 * pi * r * h + 2 * pi * r^2
        self.superficie = (2 * math.pi * self.radio * self.altura) + (2 * math.pi * (self.radio ** 2))

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Volumen = 4/3 * pi * r^3
        self.volumen = (4.0 / 3.0) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        # Superficie = 4 * pi * r^2
        self.superficie = 4.0 * math.pi * (self.radio ** 2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Volumen = (base^2 * altura) / 3
        self.volumen = ((self.base ** 2) * self.altura) / 3.0

    def calcular_superficie(self):
        # Superficie = base^2 + 2 * base * apotema
        self.superficie = (self.base ** 2) + (2.0 * self.base * self.apotema)


# ==========================================
# INTERFAZ GRÁFICA (Tkinter)
# ==========================================

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("300x200")
        self.eval('tk::PlaceWindow . center') # Centrar ventana
        self.resizable(False, False)

        # Etiqueta principal
        lbl_titulo = tk.Label(self, text="Seleccione una figura:", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=15)

        # Botones para abrir cada figura
        btn_cilindro = tk.Button(self, text="Cilindro", width=15, command=self.abrir_cilindro)
        btn_cilindro.pack(pady=5)

        btn_esfera = tk.Button(self, text="Esfera", width=15, command=self.abrir_esfera)
        btn_esfera.pack(pady=5)

        btn_piramide = tk.Button(self, text="Pirámide", width=15, command=self.abrir_piramide)
        btn_piramide.pack(pady=5)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)

class VentanaCilindro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("280x250")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cm):").pack(pady=5)
        self.txt_radio = tk.Entry(self)
        self.txt_radio.pack()

        tk.Label(self, text="Altura (cm):").pack(pady=5)
        self.txt_altura = tk.Entry(self)
        self.txt_altura.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=15)

        self.lbl_volumen = tk.Label(self, text="Volumen: ")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie: ")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            radio = float(self.txt_radio.get())
            altura = float(self.txt_altura.get())
            cilindro = Cilindro(radio, altura)
            
            # string.format equivalente en Python
            self.lbl_volumen.config(text=f"Volumen: {cilindro.get_volumen():.2f} cm³")
            self.lbl_superficie.config(text=f"Superficie: {cilindro.get_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

class VentanaEsfera(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cm):").pack(pady=5)
        self.txt_radio = tk.Entry(self)
        self.txt_radio.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=15)

        self.lbl_volumen = tk.Label(self, text="Volumen: ")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie: ")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            radio = float(self.txt_radio.get())
            esfera = Esfera(radio)
            
            self.lbl_volumen.config(text=f"Volumen: {esfera.get_volumen():.2f} cm³")
            self.lbl_superficie.config(text=f"Superficie: {esfera.get_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

class VentanaPiramide(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("280x300")
        self.resizable(False, False)

        tk.Label(self, text="Base (cm):").pack(pady=5)
        self.txt_base = tk.Entry(self)
        self.txt_base.pack()

        tk.Label(self, text="Altura (cm):").pack(pady=5)
        self.txt_altura = tk.Entry(self)
        self.txt_altura.pack()

        tk.Label(self, text="Apotema (cm):").pack(pady=5)
        self.txt_apotema = tk.Entry(self)
        self.txt_apotema.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=15)

        self.lbl_volumen = tk.Label(self, text="Volumen: ")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie: ")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            base = float(self.txt_base.get())
            altura = float(self.txt_altura.get())
            apotema = float(self.txt_apotema.get())
            piramide = Piramide(base, altura, apotema)
            
            self.lbl_volumen.config(text=f"Volumen: {piramide.get_volumen():.2f} cm³")
            self.lbl_superficie.config(text=f"Superficie: {piramide.get_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()