# Multiplicación rusa

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
summation = 0

while num1 >= 1:
    if num1 % 2 != 0:
        summation += num2
    num1 //= 2 # Se divide el primer número entre 2 y se redondea hacia abajo
    num2 *= 2
print("El resultado de la multiplicación rusa es: ", summation)