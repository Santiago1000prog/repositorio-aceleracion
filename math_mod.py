import math


def area_circulo(r: float) -> float:
    return math.pi * r * r

def mostrar_area(area: float) -> None:
    print(f"El área es de {area:.2f}")