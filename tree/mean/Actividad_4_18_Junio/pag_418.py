"""
Ejercicio Página 418: Equipo Maratón Programación
Este módulo implementa una interfaz gráfica para crear un equipo de programación
y gestionar la adición de sus programadores, aplicando validaciones de longitud 
y caracteres, además de manejar el límite de capacidad del equipo.
"""
import tkinter as tk
from tkinter import messagebox

# ==========================================
# CLASES LÓGICAS (Modelo)
# ==========================================
class Programador:
    """Clase que representa a un programador con validación estricta de texto."""
    def __init__(self, nombre, apellidos):
        self.validar_atributos(nombre, "Nombre")
        self.validar_atributos(apellidos, "Apellidos")
        self.nombre = nombre
        self.apellidos = apellidos

    def validar_atributos(self, texto, campo):
        """Valida que el texto no tenga números y su longitud sea menor a 20."""
        if len(texto) >= 20:
            # throw new Exception equivalente
            raise ValueError(f"Error en {campo}: La longitud no puede ser igual o superior a 20 caracteres.")
        
        # Simulación de charAt e isDigit de Java
        for char in texto:
            if char.isdigit():
                raise ValueError(f"Error en {campo}: No se permiten datos numéricos, solo texto.")

class EquipoMaratonProgramacion:
    """Clase que gestiona el equipo y sus integrantes."""
    def __init__(self, nombre_equipo, universidad, lenguaje, tamano):
        if tamano < 2 or tamano > 3:
            raise ValueError("El tamaño del equipo debe ser mínimo 2 y máximo 3.")
        
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []

    def equipo_completo(self):
        """Determina si el equipo está completo."""
        return len(self.programadores) >= self.tamano

    def anadir_programador(self, programador):
        """Añade un programador si hay espacio, sino lanza excepción."""
        if self.equipo_completo():
            # throw new Exception equivalente
            raise OverflowError("El equipo está completo. No se pueden añadir más programadores.")
        self.programadores.append(programador)

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaEquipo(tk.Tk):
    """Interfaz gráfica principal."""
    def __init__(self):
        super().__init__()

        self.title("Maratón de Programación")
        self.geometry("450x550")
        self.resizable(False, False)
        
        self.equipo = None # Variable para almacenar la instancia del equipo
        
        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')

    def _crear_componentes(self):
        # --- SECCIÓN 1: DATOS DEL EQUIPO ---
        tk.Label(self, text="--- DATOS DEL EQUIPO ---", font=("Arial", 10, "bold")).place(x=20, y=10)
        
        tk.Label(self, text="Nombre del Equipo:").place(x=20, y=40)
        self.txt_nom_equipo = tk.Entry(self)
        self.txt_nom_equipo.place(x=150, y=40, width=270)

        tk.Label(self, text="Universidad:").place(x=20, y=70)
        self.txt_universidad = tk.Entry(self)
        self.txt_universidad.place(x=150, y=70, width=270)

        tk.Label(self, text="Lenguaje:").place(x=20, y=100)
        self.txt_lenguaje = tk.Entry(self)
        self.txt_lenguaje.place(x=150, y=100, width=270)

        tk.Label(self, text="Tamaño (2 o 3):").place(x=20, y=130)
        self.txt_tamano = tk.Entry(self)
        self.txt_tamano.place(x=150, y=130, width=80)

        self.btn_crear_eq = tk.Button(self, text="Crear Equipo", command=self.action_crear_equipo)
        self.btn_crear_eq.place(x=150, y=160, width=120, height=30)

        # --- SECCIÓN 2: DATOS DE PROGRAMADORES ---
        tk.Label(self, text="--- AÑADIR PROGRAMADOR ---", font=("Arial", 10, "bold")).place(x=20, y=210)

        tk.Label(self, text="Nombres:").place(x=20, y=240)
        self.txt_nom_prog = tk.Entry(self, state=tk.DISABLED)
        self.txt_nom_prog.place(x=150, y=240, width=270)

        tk.Label(self, text="Apellidos:").place(x=20, y=270)
        self.txt_ape_prog = tk.Entry(self, state=tk.DISABLED)
        self.txt_ape_prog.place(x=150, y=270, width=270)

        self.btn_anadir_prog = tk.Button(self, text="Añadir Programador", state=tk.DISABLED, command=self.action_anadir_programador)
        self.btn_anadir_prog.place(x=150, y=300, width=150, height=30)

        # --- SECCIÓN 3: CONSOLA DE RESULTADOS ---
        self.txt_consola = tk.Text(self, state=tk.DISABLED, bg="#f5f5f5", font=("Consolas", 9))
        self.txt_consola.place(x=20, y=350, width=400, height=180)

    def log_consola(self, mensaje):
        """Añade un mensaje a la consola de texto."""
        self.txt_consola.config(state=tk.NORMAL)
        self.txt_consola.insert(tk.END, mensaje + "\n")
        self.txt_consola.see(tk.END)
        self.txt_consola.config(state=tk.DISABLED)

    def action_crear_equipo(self):
        try:
            nom = self.txt_nom_equipo.get().strip()
            uni = self.txt_universidad.get().strip()
            leng = self.txt_lenguaje.get().strip()
            tam = int(self.txt_tamano.get().strip())

            if not nom or not uni or not leng:
                messagebox.showwarning("Campos Vacíos", "Llene todos los datos del equipo.")
                return

            # Instanciar el equipo
            self.equipo = EquipoMaratonProgramacion(nom, uni, leng, tam)
            self.log_consola(f">> Equipo '{nom}' creado con éxito. Capacidad: {tam} miembros.")
            
            # Habilitar campos de programador y deshabilitar los de equipo
            self.txt_nom_prog.config(state=tk.NORMAL)
            self.txt_ape_prog.config(state=tk.NORMAL)
            self.btn_anadir_prog.config(state=tk.NORMAL)
            
            self.btn_crear_eq.config(state=tk.DISABLED)
            self.txt_nom_equipo.config(state=tk.DISABLED)
            self.txt_universidad.config(state=tk.DISABLED)
            self.txt_lenguaje.config(state=tk.DISABLED)
            self.txt_tamano.config(state=tk.DISABLED)

        except ValueError as e:
            # Captura error de int() o de tamaño fuera de rango
            messagebox.showerror("Error en Creación", "Tamaño inválido. Ingrese 2 o 3.")

    def action_anadir_programador(self):
        nombre = self.txt_nom_prog.get().strip()
        apellidos = self.txt_ape_prog.get().strip()

        if not nombre or not apellidos:
            messagebox.showwarning("Campos Vacíos", "Llene nombre y apellidos.")
            return

        try:
            # Validar y crear programador
            nuevo_prog = Programador(nombre, apellidos)
            
            # Añadir al equipo
            self.equipo.anadir_programador(nuevo_prog)
            
            self.log_consola(f">> Añadido: {nombre} {apellidos}.")
            
            # Limpiar campos
            self.txt_nom_prog.delete(0, tk.END)
            self.txt_ape_prog.delete(0, tk.END)

            # Informar si ya se llenó el equipo tras añadirlo
            if self.equipo.equipo_completo():
                self.log_consola(">> EL EQUIPO ESTÁ COMPLETO.")
                messagebox.showinfo("Equipo Completo", "Se ha alcanzado la capacidad máxima del equipo.")

        except ValueError as e:
            # Excepción por números o longitud
            self.log_consola(f"!! EXCEPCIÓN: {e}")
            messagebox.showerror("Validación de Texto", str(e))
            
        except OverflowError as e:
            # Excepción por equipo lleno
            self.log_consola(f"!! EXCEPCIÓN: {e}")
            messagebox.showerror("Equipo Lleno", str(e))

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    app = VentanaEquipo()
    app.mainloop()