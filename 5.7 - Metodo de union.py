# Metodo de union

formato_factura = ("No. 2025-0", "-1010 (ID: )", ")")
numero = "275"
numero_factura = numero.join(formato_factura)
print(numero_factura)

palabras = ["Hola", "Mundo", "Python"]
frase = "-".join(palabras)
print(frase)