# Declaración de un diccionario
dictionario = {"nombre": "Juan", "edad": 30, "hombre": True}

# Acceso a los valores del diccionario
print(dictionario["nombre"])  # Imprime: Juan

# Modificación de un valor en el diccionario
dictionario["edad"] = 31

# Eliminación de un par clave-valor
del dictionario["hombre"]

# Agregar un nuevo par clave-valor
dictionario["ciudad"] = "Madrid"

print(dictionario)