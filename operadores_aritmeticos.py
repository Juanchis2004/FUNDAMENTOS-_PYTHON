#Operadores Aritméticos

import math
import random

a = 3
b = 2

#Suma
suma = a + b
print(f"La suma de {a} y {b} es: {suma}")

#Resta
resta = a - b
print(f"La resta de {a} y {b} es: {resta}")

#Multiplicación
multiplicacion = a * b
print(f"La multiplicación de {a} y {b} es: {multiplicacion}")

#División
division = a / b
print(f"La división de {a} y {b} es: {division}")

#Módulo
modulo = a % b
print(f"El módulo de {a} y {b} es: {modulo}")

#División entera
division_entera = a // b
print(f"La división entera de {a} y {b} es: {division_entera}")

#Potencia
potencia = a ** b
print(f"La potencia de {a} elevado a {b} es: {potencia}")

#procendencia de operadores
resultado = a + b * 2
print(f"El resultado de la expresión ({a} + {b} * 2) es: {resultado}")

resultado_2 = (a + b) * 2
print(f"El resultado de la expresión (({a} + {b}) * 2) es: {resultado_2}")

resultado_3 = a * b // 3
print(f"El resultado de la expresión ({a} * {b} // 3) es: {resultado_3}")

resultado_4 = (a + b) // 3
print(f"El resultado de la expresión (({a} + {b}) // 3) es: {resultado_4}")

resultado_5 = a * (b // 3)
print(f"El resultado de la expresión ({a} * ({b} // 3)) es: {resultado_5}")

ejercicio = ((a + b) * (a - b) / (a * b)) - (a ** b % 3)
print(f"El resultado de la expresión (({a} + {b}) * ({a} - {b}) / ({a} * {b})) - ({a} ** {b} % 3) es: {ejercicio}")

print(math.pi)
print(math.e)
print(math.sqrt(16))

#print(random.random())
random_number = random.randint(1, 10)  
print(random_number)