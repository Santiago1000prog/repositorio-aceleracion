import math_mod
import salida


def suma(a: int, b: int) -> int:
    return a + b


def resta(a: int, b: int) -> int:
    return a - b


def pot(base: int, ex: int) -> int:
    mult = base
    for _ in range(ex - 1):
        base *= mult
    return base


print(f"{math_mod.area_circulo(17):.2f}")
print(pot(2, 3))
salida.mostrar(pot(3, 2), "Saludo en rama")
