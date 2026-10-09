# ==========================================
# Proyecto: Sistema de Calificaciones
# Asignatura: Introducción a la Programación (ITLA)
# ==========================================

# 1. Definición del arreglo o vector con al menos 5 elementos
calificaciones = [85, 67, 92, 74, 58]

print("==========================================")
print("       SISTEMA DE CALIFICACIONES          ")
print("==========================================")
print(f"Vector inicial de calificaciones: {calificaciones}\n")

# 2. Mostrar todas las calificaciones usando un ciclo (for)
print("--- 1. Mostrar todas las calificaciones ---")
for i in range(len(calificaciones)):
    print(f"Estudiante {i + 1} (Índice {i}): {calificaciones[i]}")

# 3. Acceso a un elemento específico mediante su índice
print("\n--- 2. Mostrar calificación por índice específico ---")
indice_buscado = 2
print(f"La calificación en el índice [{indice_buscado}] es: {calificaciones[indice_buscado]}")

# 4. Operación de cálculo: Cálculo del promedio
suma_notas = 0
for nota in calificaciones:
    suma_notas += nota
promedio = suma_notas / len(calificaciones)
print(f"\n--- 3. Cálculo del promedio ---")
print(f"El promedio general de la clase es: {promedio:.2f}")

# 5. Búsqueda de la calificación más alta y más baja
nota_alta = calificaciones[0]
nota_baja = calificaciones[0]

for nota in calificaciones:
    if nota > nota_alta:
        nota_alta = nota
    if nota < nota_baja:
        nota_baja = nota

print(f"\n--- 4 & 5. Calificaciones extrema ---")
print(f"Calificación más alta: {nota_alta}")
print(f"Calificación más baja: {nota_baja}")

# 6 & 7. Condicionales 'if' para contar aprobados y reprobados (Aprobación >= 70)
aprobados = 0
reprobados = 0

for nota in calificaciones:
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

print(f"\n--- 6 & 7. Conteo de Aprobados y Reprobados ---")
print(f"Estudiantes aprobados (>= 70): {aprobados}")
print(f"Estudiantes reprobados (< 70): {reprobados}")

# 8. Modificación de una calificación utilizando su índice
print("\n--- 8. Modificación de una calificación ---")
print(f"Calificación anterior en el índice 1: {calificaciones[1]}")
calificaciones[1] = 90  # Cambiamos el 67 por un 90
print(f"Calificación actualizada en el índice 1: {calificaciones[1]}")

# 9. Mostrar nuevamente el vector actualizado
print("\n--- 9. Vector actualizado ---")
print(f"Nuevas calificaciones: {calificaciones}")
print("==========================================")
