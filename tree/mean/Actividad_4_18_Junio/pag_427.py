"""
Ejercicio Página 427: Leer Archivo
Este módulo implementa una interfaz gráfica que simula la lectura de un 
archivo de texto mediante un flujo de bytes (byte stream), capturando 
las excepciones de E/S (IOException).
"""
import tkinter as tk
from tkinter import messagebox
import os

# ==========================================
# CLASE LÓGICA (Modelo)
# ==========================================
class LeerArchivo:
    """Clase estática encargada de la lectura del archivo a nivel de bytes."""

    @staticmethod
    def leer_flujo_bytes(ruta_archivo):
        """
        Simula la cadena: FileInputStream -> InputStreamReader -> BufferedReader
        Lee el archivo en modo binario ('rb') y decodifica cada línea.
        """
        contenido_leido = ""
        
        try:
            # open(..., 'rb') simula el FileInputStream (Flujo de bytes puro)
            with open(ruta_archivo, 'rb') as flujo_bytes:
                
                # Iterar sobre el archivo simula el comportamiento de BufferedReader.readLine()
                for linea_bytes in flujo_bytes:
                    
                    # decode('utf-8') simula el InputStreamReader (convierte byte a char)
                    linea_texto = linea_bytes.decode('utf-8')
                    contenido_leido += linea_texto
                    
            # La declaración 'with' llama automáticamente al método close() al terminar
            
        except FileNotFoundError:
            # Excepción específica si no existe el archivo
            raise IOError(f"El archivo '{ruta_archivo}' no fue encontrado en el sistema.")
            
        except IOError as e:
            # Equivalente a la IOException de Java para errores generales de Entrada/Salida
            raise IOError(f"Excepción de E/S al intentar leer el archivo: {str(e)}")

        return contenido_leido

# ==========================================
# CLASE INTERFAZ GRÁFICA (Vista/Controlador)
# ==========================================
class VentanaLeerArchivo(tk.Tk):
    """Interfaz gráfica para leer archivos de texto."""
    def __init__(self):
        super().__init__()

        self.title("Lector de Archivos (Flujo de Bytes)")
        self.geometry("450x400")
        self.resizable(False, False)
        
        self._crear_componentes()
        self.eval('tk::PlaceWindow . center')
        
        # Crear un archivo de prueba automáticamente para facilitar la evaluación
        self._crear_archivo_prueba()

    def _crear_archivo_prueba(self):
        """Crea un 'prueba.txt' en la carpeta actual si no existe para que el programa funcione."""
        if not os.path.exists("prueba.txt"):
            with open("prueba.txt", "w", encoding="utf-8") as f:
                f.write("¡Hola, equipo de POO!\n")
                f.write("Este es el contenido del archivo prueba.txt.\n")
                f.write("Ha sido leído a través de un flujo de bytes en Python.")

    def _crear_componentes(self):
        # Etiqueta y campo para la ruta
        tk.Label(self, text="Nombre/Ruta del archivo:").place(x=20, y=20)
        
        self.txt_ruta = tk.Entry(self)
        self.txt_ruta.place(x=170, y=20, width=150)
        self.txt_ruta.insert(0, "prueba.txt") # Valor por defecto

        # Botones
        btn_leer = tk.Button(self, text="Leer Archivo", command=self.action_leer)
        btn_leer.place(x=330, y=17, width=100, height=25)

        btn_limpiar = tk.Button(self, text="Limpiar Pantalla", command=self.action_limpiar)
        btn_limpiar.place(x=20, y=55, width=410, height=25)

        # Área de texto para visualizar el contenido
        self.txt_contenido = tk.Text(self, state=tk.DISABLED, bg="#ffffff", fg="#000000", font=("Consolas", 10))
        self.txt_contenido.place(x=20, y=90, width=410, height=280)

    def action_leer(self):
        """Intenta leer el archivo y mostrarlo en el área de texto."""
        ruta = self.txt_ruta.get().strip()
        
        if not ruta:
            messagebox.showwarning("Campo Vacío", "Por favor indique el nombre del archivo.")
            return

        try:
            # Llamado al método estático
            contenido = LeerArchivo.leer_flujo_bytes(ruta)
            
            # Mostrar en pantalla
            self.txt_contenido.config(state=tk.NORMAL)
            self.txt_contenido.delete(1.0, tk.END)
            self.txt_contenido.insert(tk.END, contenido)
            self.txt_contenido.config(state=tk.DISABLED)
            
        except IOError as e: # Captura la excepción de E/S
            messagebox.showerror("IOException", str(e))
            self.txt_contenido.config(state=tk.NORMAL)
            self.txt_contenido.delete(1.0, tk.END)
            self.txt_contenido.insert(tk.END, f"--- ERROR DE E/S ---\n{str(e)}")
            self.txt_contenido.config(state=tk.DISABLED)

    def action_limpiar(self):
        """Borra el contenido de la pantalla de lectura."""
        self.txt_contenido.config(state=tk.NORMAL)
        self.txt_contenido.delete(1.0, tk.END)
        self.txt_contenido.config(state=tk.DISABLED)

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    app = VentanaLeerArchivo()
    app.mainloop()