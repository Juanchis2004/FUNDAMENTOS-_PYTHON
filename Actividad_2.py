# Actividad 2: Calculadora de Notas
# Objetivo:
# 1) Pedir 3 notas parciales al usuario (float)
# 2) Calcular el promedio (división)
# 3) Calcular cuántos puntos faltan para llegar a la nota máxima (5.0) usando resta
# 4) Determinar si aprueba (promedio >= 3.0) usando comparación
# 5) Mostrar todos los resultados con formato legible y redondear el promedio a 2 decimales usando round()

def pedir_nota(mensaje):
    """
    Pide una nota al usuario (float) y valida que NO sea mayor a 5.
    Si la nota es mayor a 5, vuelve a pedirla.
    """
    nota = float(input(mensaje))

    # Validación: la nota no debe de pasar de 5.0
    while nota > 5.0:
        print(" 😠La nota no puede ser mayor a 5.0. 😊Intentalo de nuevo aprendiz.")
        nota = float(input(mensaje))

    return nota

nota1 = pedir_nota("Ingrese la primera nota: ")
nota2 = pedir_nota("Ingrese la segunda nota: ")
nota3 = pedir_nota("Ingrese la tercera nota: ")

suma_notas = nota1 + nota2 + nota3


promedio = suma_notas / 3


promedio = round(promedio, 2)


puntos_faltantes = 5.0 - promedio


if puntos_faltantes < 0:
    puntos_faltantes = 0.0

aprueba = promedio >= 3.0
print("\n" + "=" * 45)
print("Resultado Final")
print("=" * 45)

print(f"1) Nota 1: {round(nota1, 2):.2f}")
print(f"2) Nota 2: {round(nota2, 2):.2f}")
print(f"3) Nota 3: {round(nota3, 2):.2f}")

print("-" * 45)
print(f"Promedio (redondeado): {promedio:.2f}")
print(f"Puntos faltantes para 5.0: {round(puntos_faltantes, 2):.2f}")
print(f"¿Aprueba?: {'Sí😁' if aprueba else 'No😓'}")

print("=" * 45)

