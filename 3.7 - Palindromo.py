word = input("Ingrese una palabra: ")
if word == word[::-1]: # Se compara la palabra con su reverso
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")