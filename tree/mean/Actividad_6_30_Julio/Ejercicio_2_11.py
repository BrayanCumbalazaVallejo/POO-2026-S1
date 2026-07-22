"""
Ejercicio 2.11: Sobrecarga de Constructores (Clase ArticuloCientifico)
"""

class ArticuloCientifico:
    # 1. Primer constructor (Constructor base en Python: __init__)
    def __init__(self, nombre, autor):
        self.nombre = nombre
        self.autor = autor
        # Valores por defecto para los demás atributos
        self.palabras_claves = "No definido"
        self.nombre_publicacion = "No definido"
        self.anio = 0
        self.resumen = "No definido"
        
    # 2. Segundo constructor (Invoca al primero)
    @classmethod
    def desde_cinco_parametros(cls, nombre, autor, palabras_claves, nombre_publicacion, anio):
        # Invoca al primer constructor (cls llama a __init__)
        instancia = cls(nombre, autor)
        instancia.palabras_claves = palabras_claves
        instancia.nombre_publicacion = nombre_publicacion
        instancia.anio = anio
        return instancia
        
    # 3. Tercer constructor (Invoca al segundo)
    @classmethod
    def desde_seis_parametros(cls, nombre, autor, palabras_claves, nombre_publicacion, anio, resumen):
        # Invoca al segundo constructor (desde_cinco_parametros)
        instancia = cls.desde_cinco_parametros(nombre, autor, palabras_claves, nombre_publicacion, anio)
        instancia.resumen = resumen
        return instancia
        
    def imprimir_atributos(self):
        """Método que imprime los atributos del artículo en pantalla."""
        print("\n" + "=" * 50)
        print("       DATOS DEL ARTÍCULO CIENTÍFICO")
        print("=" * 50)
        print(f"Título:         {self.nombre}")
        print(f"Autor:          {self.autor}")
        print(f"Palabras Clave: {self.palabras_claves}")
        print(f"Publicación:    {self.nombre_publicacion}")
        print(f"Año:            {self.anio}")
        print(f"Resumen:        {self.resumen}")
        print("=" * 50 + "\n")


# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (Método main)
# ==========================================
if __name__ == "__main__":
    print("-" * 50)
    print("REGISTRO DE ARTÍCULO CIENTÍFICO")
    print("-" * 50)
    print("Por favor, ingrese los metadatos del artículo:\n")
    
    try:
        nombre_in = input("1. Nombre del artículo: ")
        autor_in = input("2. Autor del artículo: ")
        palabras_in = input("3. Palabras claves (separadas por coma): ")
        publicacion_in = input("4. Nombre de la publicación: ")
        anio_in = int(input("5. Año de publicación (ej. 2026): "))
        resumen_in = input("6. Resumen: ")
        
        # El enunciado pide instanciar utilizando el TERCER constructor
        articulo = ArticuloCientifico.desde_seis_parametros(
            nombre_in, autor_in, palabras_in, publicacion_in, anio_in, resumen_in
        )
        
        # Imprimir los valores de los atributos en pantalla
        articulo.imprimir_atributos()
        
    except ValueError:
        print("\n[Error] El año de publicación debe ser un valor numérico entero.")