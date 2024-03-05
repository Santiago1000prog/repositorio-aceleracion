import math_mod


def suma(a: int, b: int) -> int:
    return a + b


def pot(base: int, ex: int) -> int:
    mult = base
    for _ in range(ex - 1):
        base *= mult
    return base


print(f"{math_mod.area_circulo(10):.2f}")
print(pot(9, 3))
