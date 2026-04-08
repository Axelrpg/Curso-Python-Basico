# Metodos de separacion

# Metodo de particion
tupla = "https://www.ejemplo.com".partition("://")
print(tupla)
protocolo, separador, dominio = tupla
print("Protocolo: {0}\nDominio: {1}".format(protocolo, dominio))

# Metodo de splitlines
texto = """Línea 1
Línea 2
Línea 3
Línea 4
"""
print(texto.splitlines())

# Metodo de split
frase = "Hola Mundo Python"
print(frase.split())
mi_cadena = "Python,Java,C++"
print(mi_cadena.split(","))
print(mi_cadena.split(",", maxsplit=1))

# Metodo de rsplit
mi_cadena = "Python,Java,C++"
print(mi_cadena.rsplit(",", maxsplit=1))
