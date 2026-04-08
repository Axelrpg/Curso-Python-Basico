# Metodos de sustitucion

palabra = "manejo de cadenas en python"

# Formatear cadena con formato
print("La palabra es: {}".format(palabra))

# Reemplazar una subcadena por otra
print(palabra.replace("python", "programacion"))

# Eliminar espacios al inicio y al final
palabra_con_espacios = "   manejo de cadenas en python con espacios   "
print(palabra_con_espacios.strip())

# Eliminar espacios al inicio
print(palabra_con_espacios.lstrip())

# Eliminar espacios al final
print(palabra_con_espacios.rstrip())