# Formateo de salida de datos numericos

archivo = "mongoDB.txt"
path = rf"C:\Users\Usuario\Desktop\Python\{archivo}"
print(f"El archivo se encuentra en: {path}")

pi = 3.141592653589793
piFormateado = f"{pi:.2f}"
print(f"El valor de pi con dos decimales es: {piFormateado}")

lenguaje = "Python"
lenguajeFormateado = f"{lenguaje:>10}"
print(f"El lenguaje formateado es: '{lenguajeFormateado}'")

numFormateado = 42
numFormateado = f"{numFormateado:06}"
print(f"El número formateado es: {numFormateado}")

plataforma = "MOOC"
plataformaFormateada = f"{plataforma:_<10}"
print(f"La plataforma formateada es: '{plataformaFormateada}'")