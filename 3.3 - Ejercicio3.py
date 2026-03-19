number = int(input("Ingrese un número entero entre 1 y 10: "))
if number <= 5:
    print("El número es pequeño.")
elif number > 5 and number < 10:
    print("El número es mediano.")
elif number >= 10:
    print("El número es grande.")
