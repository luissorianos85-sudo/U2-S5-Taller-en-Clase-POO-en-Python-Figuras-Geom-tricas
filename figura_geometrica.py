""" 20/11/2025
class Figura_Geometrica:
"""
# figura_geometrica.py
class FiguraGeometrica:
    """
    Superclase que representa una figura geométrica.
    Implementando encapsulamiento con validaciones en alto y ancho.
    """

    def __init__(self, ancho: float, alto: float):
        self._ancho = 0.0
        self._alto = 0.0
        # Usamos los setters para aplicar las validaciones al inicio
        self.ancho = ancho
        self.alto = alto

    # --- Getters y Setters con Encapsulamiento y Validaciones ---

    @property
    def ancho(self) -> float:
        """Getter para el atributo privado _ancho"""
        return self._ancho

    @ancho.setter
    def ancho(self, valor: float):
        """Setter para _ancho con validación"""
        if valor <= 0:
            # Levantar ValueError si es menor o igual a 0
            raise ValueError(f"El ancho debe ser mayor que 0. Valor recibido: {valor}")
        self._ancho = valor

    @property
    def alto(self) -> float:
        """Getter para el atributo privado _alto."""
        return self._alto

    @alto.setter
    def alto(self, valor: float):
        """Setter para _alto con validación."""
        if valor <= 0:
            # Levantar ValueError si es menor o igual a 0
            raise ValueError(f"El alto debe ser mayor que 0. Valor recibido: {valor}")
        self._alto = valor

    # --- Métodos de Figura ---

    def area(self) -> float:
        """Calcula el área: ancho * alto."""
        return self.ancho * self.alto

    def perimetro(self):
        """No implementado en la clase base. De acuerdo a la instrucción."""
        # Se usa 'pass' para dejar el cuerpo del método vacío
        pass
    # --- Método Especial __str__ ---

    def __str__(self):
        """Devuelve la representación en cadena con dimensiones."""
        return f"FiguraGeometrica [Ancho: {self.ancho:.2f}, Alto: {self.alto:.2f}]"

if __name__ == "__main__":
    # 1. Prueba de area()
    figura_base = FiguraGeometrica(ancho=5.0, alto=3.0)
    print(figura_base)

    area_calculada = figura_base.area()
    print(f"Objeto: {figura_base}")
    print(f"Área calculada (5.0 * 3.0): {area_calculada:.2f}")
    # Resultado esperado: 15.00

    # 2. Prueba de perimetro()
    print("Intentando llamar a perimetro() en la clase base (debe fallar)...")
    
