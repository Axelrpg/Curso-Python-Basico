# Programa que calcule las reaices de una ecuación de segundo grado mediante la formula general, utilizando if y elif para determinar el tipo de raices

import math

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

discriminating = (b**2) - (4 * a * c)
if discriminating > 0:
    root1 = (-b + math.sqrt(discriminating)) / (2 * a)
    root2 = (-b - math.sqrt(discriminating)) / (2 * a)
    print("Las raíces son reales y diferentes:", round(root1, 2), "y", round(root2, 2))
elif discriminating == 0:
    root = -b / (2 * a)
    print("Las raíces son reales e iguales: ", round(root, 2))
else:
    print("Las raíces son complejas y conjugadas.")
