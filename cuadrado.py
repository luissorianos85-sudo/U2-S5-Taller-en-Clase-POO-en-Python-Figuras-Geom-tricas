""" 20/11/2025"""
# cuadrado.py
from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    """
    Clase que representa un Cuadrado. Hereda de FiguraGeometrica.
    """

    def __init__(self, lado: float):
        """
        El constructor recibe solo 'lado' y lo asigna a ancho y alto.
        """
        # Inicializa la superclase con el mismo valor para ancho y alto
        super().__init__(lado, lado)

    # --- Sobrescritura de Setters (para mantener la condición de Cuadrado) ---

    # Sobrescribimos el setter de ancho de la superclase
    @FiguraGeometrica.ancho.setter
    def ancho(self, valor: float):
        """Sobreescribe el setter de ancho, asegurando que alto también cambie."""
        if valor <= 0:
            raise ValueError(f"El lado (ancho) debe ser un valor positivo. Valor recibido: {valor}")
        self._ancho = valor
        self._alto = valor  # Mantiene la condición de Cuadrado

    # Sobrescribimos el setter de alto de la superclase
    @FiguraGeometrica.alto.setter
    def alto(self, valor: float):
        """Sobreescribe el setter de alto, asegurando que ancho también cambie."""
        if valor <= 0:
            raise ValueError(f"El lado (alto) debe ser un valor positivo. Valor recibido: {valor}")
        self._alto = valor
        self._ancho = valor  # Mantiene la condición de Cuadrado

    # --- Sobrescritura de Métodos ---

    def area(self) -> float:
        """Sobreescribe el cálculo del área (lado * lado)."""
        return self.ancho * self.alto

    def perimetro(self) -> float:
        """Sobreescribe el cálculo del perímetro (4 * lado)."""
        return 4 * self.ancho

    def __str__(self) -> str:
        """Sobreescribe la representación en cadena[cite: 77]."""
        return f"Cuadrado [Lado: {self.ancho:.2f}] - Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}"


if __name__ == '__main__':
    # --- 1. Prueba de Creación e Información Inicial ---
    print("--- 1. Prueba de Creación e Información Inicial ---")
    lado_inicial = 6.0
    try:
        cuadrado1 = Cuadrado(lado=lado_inicial)
        print(f"Objeto creado: {cuadrado1}")
        print(f"Ancho inicial: {cuadrado1.ancho:.2f}, Alto inicial: {cuadrado1.alto:.2f}")
    except ValueError as e:
        print(f"Error al crear: {e}")

    print("-" * 45)

    # --- 2. Prueba de Sobrescritura de Setters (Mantenimiento de la condición) ---
    print("--- 2. Prueba de Setters y Mantenimiento de la Igualdad ---")

    # a) Cambiar el ancho
    nuevo_ancho = 10.5
    print(f"Cambiando ancho a {nuevo_ancho:.2f}...")
    try:
        cuadrado1.ancho = nuevo_ancho
        print(f"Nuevo Ancho: {cuadrado1.ancho:.2f}")
        print(f"Nuevo Alto (debe ser igual): {cuadrado1.alto:.2f}")
        print(f"Nueva Área: {cuadrado1.area():.2f}, Nuevo Perímetro: {cuadrado1.perimetro():.2f}")
    except ValueError as e:
        print(f"Error al cambiar ancho: {e}")

    print("-" * 45)

    # b) Cambiar el alto
    nuevo_alto = 3.25
    print(f"Cambiando alto a {nuevo_alto:.2f}...")
    try:
        cuadrado1.alto = nuevo_alto
        print(f"Nuevo Alto: {cuadrado1.alto:.2f}")
        print(f"Nuevo Ancho (debe ser igual): {cuadrado1.ancho:.2f}")
        print(f"Nueva Área: {cuadrado1.area():.2f}, Nuevo Perímetro: {cuadrado1.perimetro():.2f}")
    except ValueError as e:
        print(f"Error al cambiar alto: {e}")

    print("-" * 45)