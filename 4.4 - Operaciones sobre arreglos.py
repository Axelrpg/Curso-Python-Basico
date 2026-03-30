# Declarar
vector = [1, 2, 3, 4, 5]

# Mostrar
print(vector)

# Cambiar valor
vector[2] = 10

# Indices negativos
vector[-2] = 20

# Sumar y multiplicar
vector = vector + [6, 7]
vector = vector * 2

# Recorrer
for i in vector:
    print(i)

# Crear una matriz
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0][1] = 10

for row in matrix:
    for element in row:
        print(element)
