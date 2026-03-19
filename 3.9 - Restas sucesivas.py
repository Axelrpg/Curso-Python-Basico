num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
quotient = 0

while num1 >= num2:
    num1 -= num2
    quotient += 1

print("El resultado de la división es:", quotient, "con un residuo de:", num1)
