name = input("Ingrese el nombre del empleado: ")
hours_worked = float(input("Ingrese las horas trabajadas: "))
salary = 5500
salary_per_hour = 135

if hours_worked == 40:
    print("El salario semanal de", name, "es: ", (salary))
elif hours_worked < 40:
    print("El salario semanal de", name, "es: ", (hours_worked * salary_per_hour))
else:
    extra_hours = hours_worked - 40
    print(
        "El salario semanal de",
        name,
        "es: ",
        salary + (extra_hours * salary_per_hour),
    )
