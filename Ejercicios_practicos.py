# =========================
# Condicionales - Ejercicio 1 (sencillo)
# Crear variables según criterio:
# - Nombre de una persona
# - Valor de un producto
# - Promedio de una asignatura
# - Imprimir en consola las variables creadas
# =========================

import math

nombre_persona = "Juan"
valor_producto = 25000
promedio_asignatura = 4.2

print("\n--- Ejercicio 1 ---")
print(nombre_persona)
print(valor_producto)
print(promedio_asignatura)

# =========================
# Condicionales - Ejercicio 2
# Crear programa que lee tipos de datos y los relaciona con operadores:
# - dos enteros
# - un float
# - dos String
#
# Requisitos:
# 1) sumar los tres números y mostrar en pantalla
# 2) visualizar el entero mayor
# 3) visualizar la división del float con el resto de la división de los dos enteros
# 4) visualizar la concatenación de las dos cadenas leídas
# =========================

entero1 = int(input("\nIngresa el primer entero: "))
entero2 = int(input("Ingresa el segundo entero: "))
float_num = float(input("Ingresa un numero float: "))

cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

suma_tres = entero1 + entero2 + float_num
print("\n--- Ejercicio 2 ---")
print(f"Suma de los tres numeros: {suma_tres}")

if entero1 > entero2:
    mayor = entero1
else:
    mayor = entero2
print(f"Entero mayor: {mayor}")

resto_enteros = entero1 % entero2
division_float_con_resto = float_num / resto_enteros
print(f"División del float entre el resto de la división de los enteros: {division_float_con_resto}")

concatenacion = cadena1 + cadena2
print(f"Concatenación de cadenas: {concatenacion}")

# =========================
# Ejercicio 3
# Crear 2 variables enteras: base y exponente
# Calcular la potencia y mostrar el resultado
# =========================

base = 2
exponente = 5

potencia = base ** exponente
print("\n--- Ejercicio 3 ---")
print(f"Base: {base}")
print(f"Exponente: {exponente}")
print(f"Potencia (base^exponente): {potencia}")

# =========================
# Ejercicio 4
# Hallar la raíz cuadrada de:
# 2, 8, 9, 27, 28, 55, 121
# y mostrar los resultados de cada operación.
# =========================

numeros = [2, 8, 9, 27, 28, 55, 121]

print("\n--- Ejercicio 4 ---")
for numero in numeros:
    raiz = math.sqrt(numero)
    print(f"sqrt({numero}) = {raiz}")

# =========================
# Ejercicio 5
# - Crear variable para almacenar nombre del estudiante
# - Crear 5 variables para 5 notas decimales
# - Calcular el promedio final (suma / 5)
# - Mostrar promedio y nombre
# =========================

nombre_estudiante = input("\n--- Ejercicio 5 ---\nIngresa el nombre del estudiante: ")

nota1 = float(input("Ingresa la primera nota decimal: "))
nota2 = float(input("Ingresa la segunda nota decimal: "))
nota3 = float(input("Ingresa la tercera nota decimal: "))
nota4 = float(input("Ingresa la cuarta nota decimal: "))
nota5 = float(input("Ingresa la quinta nota decimal: "))

promedio_final = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("\nResultados del Ejercicio 5:")
print(f"Estudiante: {nombre_estudiante}")
print(f"Promedio final: {promedio_final}")

# =========================
# Ejercicio 6
# - Crear numeroUno = 8
# - Crear numeroDos = 2
# - Intercambiar usando una variable auxiliar
# - Mostrar resultados
# =========================

numeroUno = 8
numeroDos = 2

auxiliar = numeroUno
numeroUno = numeroDos
numeroDos = auxiliar

print("\n--- Ejercicio 6 ---")
print(f"numeroUno: {numeroUno}")
print(f"numeroDos: {numeroDos}")

# =========================
# Ejercicio 7
# Crear una variable booleana llamada "Estado"
# con la operación: (5 == 2) || (2 > 1)
# Mostrar el resultado de la variable Estado.
# =========================

Estado = (5 == 2) or (2 > 1)

print("\n--- Ejercicio 7 ---")
print(f"Estado: {Estado}")

# =========================
#   Ejercicio 8
# - Crear una variable llamada "Resultado".
# - Dentro de "Resultado", crear una operación aritmética
#   usando varios operadores matemáticos en repetidas ocasiones
# - Mostrar el resultado
#
# Ejemplo parecido: (9/2) + 8*2 + 1/(2+2)
# =========================

Resultado = (9 / 2) + (8 * 2) + (1 / (2 + 2))

print("\n--- Ejercicio 8 ---")
print(f"Resultado: {Resultado}")

# =========================
# Ejercicio 9
# Cuadrado: ladoCuadrado=8 -> área y perímetro
# Triángulo: baseTriangulo=9, ladoUnoTriangulo=8, ladoDosTriangulo=8 -> área y perímetro
# Rectángulo: baseRectangulo=8, alturaRectangulo=6 -> área y perímetro
# =========================

ladoCuadrado = 8
areaCuadrado = ladoCuadrado ** 2
perimetroCuadrado = 4 * ladoCuadrado

baseTriangulo = 9
ladoUnoTriangulo = 8
ladoDosTriangulo = 8

# altura del triángulo isósceles (base=9, lados iguales=8)
# altura = sqrt(lado^2 - (base/2)^2)
alturaTriangulo = math.sqrt(ladoUnoTriangulo ** 2 - (baseTriangulo / 2) ** 2)
areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
perimetroTriangulo = baseTriangulo + ladoUnoTriangulo + ladoDosTriangulo

baseRectangulo = 8
alturaRectangulo = 6
areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = 2 * (baseRectangulo + alturaRectangulo)

print("\n--- Ejercicio 9 ---")

print("\nCuadrado:")
print(f"ladoCuadrado: {ladoCuadrado}")
print(f"Área del cuadrado: {areaCuadrado}")
print(f"Perímetro del cuadrado: {perimetroCuadrado}")

print("\nTriángulo:")
print(f"baseTriangulo: {baseTriangulo}")
print(f"ladoUnoTriangulo: {ladoUnoTriangulo}")
print(f"ladoDosTriangulo: {ladoDosTriangulo}")
print(f"Área del triángulo: {areaTriangulo}")
print(f"Perímetro del triángulo: {perimetroTriangulo}")

print("\nRectángulo:")
print(f"baseRectangulo: {baseRectangulo}")
print(f"alturaRectangulo: {alturaRectangulo}")
print(f"Área del rectángulo: {areaRectangulo}")
print(f"Perímetro del rectángulo: {perimetroRectangulo}")

# =========================
# Ejercicio 10
# Determinar categoría por edad según rangos:
# 0-5: Infante
# 6-10: Niño
# 11-15: Pre adolescente
# 16-18: Adolescente
# 19-25: Pre adulto
# 26-40: Adulto
# 41-55: Pre anciano
# 56+: Anciano
# =========================

edad = int(input("\n--- Ejercicio 10 ---\nIngresa la edad de la persona: "))

if 0 <= edad <= 5:
    categoria = "Infante"
elif 6 <= edad <= 10:
    categoria = "Niño"
elif 11 <= edad <= 15:
    categoria = "Pre adolescente"
elif 16 <= edad <= 18:
    categoria = "Adolescente"
elif 19 <= edad <= 25:
    categoria = "Pre adulto"
elif 26 <= edad <= 40:
    categoria = "Adulto"
elif 41 <= edad <= 55:
    categoria = "Pre anciano"
else:
    categoria = "Anciano"

print(f"Edad: {edad}")
print(f"Categoría: {categoria}")
