calification1 = 100.0
calification2 = 70.0

average = (calification1 + calification2) / 2

isApproved = average >= 70.0
isExcellent = average > 90.0 and calification1 > 85.0 and calification2 > 85.0

print("Promedio:", average)
print("¿Está aprobado?", isApproved)
print("¿Es excelente?", isExcellent)