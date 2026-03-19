limit = int(input("Ingrese el límite de números para la serie de Fibonacci: "))
a, b = 0, 1  # Se inicializan los dos primeros números de la serie de Fibonacci

for i in range(limit):
    print(a, end=" ")
    a, b = (
        b,
        a + b,
    )  # Se asigna el valor de b a a, y el valor de a + b a b, para obtener el siguiente número en la serie
