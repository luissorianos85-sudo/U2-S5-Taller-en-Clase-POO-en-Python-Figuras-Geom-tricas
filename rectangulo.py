# rectangulo.py
from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    """
    Clase que representa un Rectángulo. Hereda de FiguraGeometrica.
    """

    def __init__(self, ancho: float, alto: float):
        """Inicializa el rectángulo usando el constructor de la superclase."""
        super().__init__(ancho, alto)

    # --- Sobrescritura de Métodos ---

    def area(self) -> float:
        """Sobreescribe el cálculo del área (ancho * alto)."""
        return self.ancho * self.alto

    def perimetro(self) -> float:
        """Sobreescribe el cálculo del perímetro (2 * ancho + 2 * alto)."""
        return 2 * self.ancho + 2 * self.alto

    def __str__(self) -> str:
        """Sobreescribe la representación en cadena[cite: 83]."""
        return f"Rectangulo [Ancho: {self.ancho:.2f}, Alto: {self.alto:.2f}] - Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}"


if __name__ == '__main__':
    # --- 1. Prueba de Creación e Información Inicial ---
    print("--- 1. Prueba de Creación e Información Inicial ---")
    ancho_inicial = 8.0
    alto_inicial = 4.0

    try:
        # Crea un objeto Rectangulo
        rectangulo1 = Rectangulo(ancho=ancho_inicial, alto=alto_inicial)
        print(f"Objeto creado: {rectangulo1}")
        # Resultados esperados: Área: 32.00, Perímetro: 24.00

    except ValueError as e:
        print(f"Error al crear: {e}")

    print("-" * 55)

    # --- 2. Prueba de Modificación de Dimensiones (usando setters de la superclase) ---
    print("--- 2. Prueba de Modificación de Dimensiones ---")

    # a) Cambiar solo el ancho
    nuevo_ancho = 15.0
    print(f"Cambiando ancho a {nuevo_ancho:.2f} (Alto se mantiene en {rectangulo1.alto:.2f})...")
    try:
        rectangulo1.ancho = nuevo_ancho
        print(f"Nuevo Rectángulo: {rectangulo1}")
        # Resultados esperados: Área: 60.00, Perímetro: 38.00
    except ValueError as e:
        print(f"Error al cambiar ancho: {e}")

    print("-" * 55)

    # b) Cambiar solo el alto
    nuevo_alto = 2.5
    print(f"Cambiando alto a {nuevo_alto:.2f} (Ancho se mantiene en {rectangulo1.ancho:.2f})...")
    try:
        rectangulo1.alto = nuevo_alto
        print(f"Nuevo Rectángulo: {rectangulo1}")
        # Resultados esperados: Área: 37.50, Perímetro: 35.00
    except ValueError as e:
        print(f"Error al cambiar alto: {e}")

    print("-" * 55)