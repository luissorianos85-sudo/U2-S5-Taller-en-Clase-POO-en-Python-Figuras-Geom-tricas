# main.py
from cuadrado import Cuadrado
from rectangulo import Rectangulo


# from figura_geometrica import FiguraGeometrica # No necesaria para la ejecución, pero útil si se usaran directamente.

# --- Funciones de Polimorfismo  ---

def sumar_areas(figuras: list) -> float:
    """
    Recibe una lista de figuras y suma sus áreas usando Polimorfismo.
    """
    total_area = 0.0
    for figura in figuras:
        # Invoca area() sin saber el tipo específico de la figura
        total_area += figura.area()
    return total_area


def sumar_perimetros(figuras: list) -> float:
    """
    Recibe una lista de figuras y suma sus perímetros usando Polimorfismo.
    """
    total_perimetro = 0.0
    for figura in figuras:
        # Invoca perimetro() sin saber el tipo específico de la figura
        total_perimetro += figura.perimetro()
    return total_perimetro


# --- Programa Principal (Ejecución) ---

if __name__ == "__main__":

    print("===================================================================")
    print("  TALLER POO: FIGURAS GEOMÉTRICAS")
    print("===================================================================")

    # 1. Crear dos cuadrados y dos rectángulos.
    print("--- 1. Creación de Objetos Válidos ---")
    try:
        cuadrado_a = Cuadrado(lado=5.0)
        cuadrado_b = Cuadrado(lado=10.0)
        rectangulo_c = Rectangulo(ancho=4.0, alto=6.0)
        rectangulo_d = Rectangulo(ancho=8.5, alto=2.5)

        figuras = [cuadrado_a, cuadrado_b, rectangulo_c, rectangulo_d]

    except ValueError as e:
        print(f"Error al crear figuras iniciales: {e}")
        figuras = []  # Asegura que el programa no falle si la creación inicial falla

    # 3. Mostrar área, perímetro, valores, y objeto.
    print("--- 2. Mostrar valores iniciales y objeto ---")
    for i, fig in enumerate(figuras):
        print(f"Objeto {i + 1}: {fig}")  # Muestra impresión del objeto (__str__)
        print(f"   Valores (Ancho/Alto): {fig.ancho:.2f}/{fig.alto:.2f}")  # Muestra valores
        print(f"   Área: {fig.area():.2f}")  # Muestra área
        print(f"   Perímetro: {fig.perimetro():.2f}")  # Muestra perímetro

    # 2. Asignar valores inválidos para demostrar encapsulamiento (validación de errores).
    print("" + "=" * 50)
    print("--- 3. Demostración de Encapsulamiento y Validación de Errores ---")

    print("\n[Validación de Error - Cuadrado]: Intentando ancho = 0.0")
    try:
        cuadrado_a.ancho = 0.0
    except ValueError as e:
        print(f"   [Error Capturado - OK]: {e}")

    print("\n[Validación de Error - Rectángulo]: Intentando alto = -5.0")
    try:
        rectangulo_c.alto = -5.0
    except ValueError as e:
        print(f"   [Error Capturado - OK]: {e}")

    # Demostración de Modificación de Valores Válidos
    print("--- Modificación de Valores Válidos ---")
    print(f"Cuadrado A antes: {cuadrado_a}")
    cuadrado_a.ancho = 7.0  # Usa el setter sobrescrito, actualiza alto automáticamente
    print(f"Cuadrado A después (modificación de valores): {cuadrado_a}")

    print(f"Rectángulo D antes: {rectangulo_d}")
    rectangulo_d.alto = 10.0
    print(f"Rectángulo D después (modificación de valores): {rectangulo_d}")

    # --- Demostración de Polimorfismo ---
    print("" + "=" * 50)
    print("--- 4. Polimorfismo (Sumar Áreas y Perímetros) ---")

    # 1. sumar_areas
    total_areas = sumar_areas(figuras)
    print(f"La Suma Total de Áreas es: {total_areas:.2f} ")

    # 2. sumar_perimetros
    total_perimetros = sumar_perimetros(figuras)
    print(f"La Suma Total de Perímetros es: {total_perimetros:.2f} ")
    print("===================================================================")