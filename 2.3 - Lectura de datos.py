weight = float(input("Ingrese su peso en kg: "))
height = float(input("Ingrese su altura en metros: "))

bmi = weight / (height ** 2)
print("Su Índice de Masa Corporal (IMC) es:", round(bmi, 2))