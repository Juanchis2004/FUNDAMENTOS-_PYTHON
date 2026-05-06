# Actividad 3: Clasificador de IMC
# Objetivo:
# - Pedir peso (kg) y estatura (m) al usuario
# - Validar que ambos sean valores positivos (bonus)
# - Calcular el IMC: IMC = peso / (estatura ** 2)
# - Clasificar con if / elif / else:
# * Bajo peso ( < 18.5 )
# * Normal ( 18.5 - 24.9 )
# * Sobrepeso ( 25 - 29.9 )
# * Obesidad ( >= 30 )

def pedir_float(mensaje):
    """
    Pide un número al usuario y lo convierte a float.
    """
    return float(input(mensaje))

def pedir_positivo(mensaje):
    """
    Bonus:
    - Valida que el valor ingresado sea > 0.
    - Si no lo es, vuelve a pedirlo.
    """
    valor = pedir_float(mensaje)
    while valor <= 0:
        print("El valor debe ser positivo. Intenta de nuevo.")
        valor = pedir_float(mensaje)
    return valor

#1) Entrada de datos (peso y estatura)
peso = pedir_positivo("Ingrese su peso en kg:")
estatura = pedir_positivo("Ingrese su estatura en metros:")

#2) Cálculo del IMC
imc = peso / (estatura ** 2)

#3) Clasificación con if / elif / else
if imc < 18.5:
    clasificacion = "Bajo peso 🙅‍♂️"
elif imc <= 24.9:
    clasificacion = "Normal 😎"
elif imc <= 29.9:
    clasificacion = "Sobrepeso🚫"
else:
    clasificacion = "Obesidad🫥"

#4) Mostrar resultado con buena estética en consola
print("\n" + "=" * 45)
print("Clasificacion de IMC")
print("=" * 45)
print(f"Peso: {peso:.2f} kg")
print(f"Estatura: {estatura:.2f} m")
print("-" * 45)
print(f"IMC: {imc:.2f}")
print(f"Clasificacion: {clasificacion}")
print("=" * 45)
