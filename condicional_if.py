# condicional IF/ELIF/ELSE

if False:
    print("la condicion es verdadera")
elif False:
    print("la condicion es falsa")
else:
    print("la condicion es falsa")

# ejercicio: clasificacion de edad

edad = 50
if edad < 18:
    print("eres un menor de edad")
elif edad >= 18 and edad < 65:
    print("eres un adulto")
else:
    print("eres un adulto mayor")

# Ejercicio: clasificacion de edad IF anidado

edad = int(input("Ingrese su edad para ser clasificada: "))

if edad < 18:
    if edad > 12 and edad < 18:
        print("Adolescente")
    else:
        print("Niño")
else:
    if edad >= 18 and edad < 65:
        print("eres un adulto")
    else:
        print("eres un adulto mayor")

# Operador ternario

numero = 10
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

print("El numero es par") if numero % 2 == 0 else print("El numero es impar")
