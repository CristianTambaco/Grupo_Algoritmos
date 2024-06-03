print("Programa para determinar el número de estudiantes aprobados y reprobados")
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

contador_aprobados = 0
contador_reprobados = 0

for i in range(cantidad_estudiantes):
    calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
    if calificacion >= 7.0:
        contador_aprobados += 1
    else:
        contador_reprobados += 1

print(f"Estudiantes aprobados: {contador_aprobados}")
print(f"Estudiantes reprobados: {contador_reprobados}")
