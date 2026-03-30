# Declaración de una lista
lista = [1, True, "Hola"]

# Agregar elementos
lista.append(3.14)

# Insertar elementos
lista.insert(3, "Mundo")
lista.insert(5, "PI")

# Extender la lista, agregando varios elementos a la vez
lista.extend([False, 42])

# Eliminar el último elemento
value = lista.pop()
print("Valor eliminado:", value)
lista.pop()

# Eliminar un elemento específico
lista.remove("Mundo")

print(lista)