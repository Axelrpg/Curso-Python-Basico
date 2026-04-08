# Metodos de formato
palabra = "manejo de cadenas en python"
factura = "12345"

# Salto de linea
print("Hola\nMundo")

# Primera letra en mayuscula
print(palabra.capitalize())

# Todas las letras en minuscula
print(palabra.lower())

# Todas las letras en mayuscula
print(palabra.upper())

# Invertir mayusculas y minusculas
print(palabra.swapcase())

# Primera letra de cada palabra en mayuscula
print(palabra.title())

# Longitud de la cadena
print(len(palabra))

# Centrar la cadena con espacios
print(palabra.center(50, "-"))

# Alinear a la izquierda con espacios
print(palabra.ljust(50, "-"))

# Alinear a la derecha con espacios
print(palabra.rjust(50, "-"))

# Rellenar con ceros a la izquierda
print(factura.zfill(10))