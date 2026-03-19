# Números perfectos

number = int(input("¿Cuántos números desea? "))
output = ""

for i in range(1, number):
    summation = 0
    for j in range(1, i - 1):
        if i % j == 0:
            summation += j
    if summation == i:
        output += str(i) + ","
print("Los números entre 1 y", number, "son:", output)
