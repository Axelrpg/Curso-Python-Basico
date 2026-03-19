limit = int(input("Ingrese hasta que número desea encontrar los números primos: "))
output = ""
for i in range(2, limit + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1): # Se verifica si el número es divisible por algún número menor o igual a su raíz cuadrada
        if i % j == 0:
            is_prime = False
            break # Si el número es divisible por algún número menor o igual a su raíz cuadrada, no es primo y se rompe el ciclo
    if is_prime:
        output += str(i) + ","
print("Los números primos entre 1 y", limit, "son:", output)
