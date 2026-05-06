# JUEGO DE ADIVINANZA (1 a 100)
# El programa elige un número secreto aleatorio entre 1 y 100.
# Tu tarea es adivinarlo ingresando números por consola.
# Si te equivocas, te dice si vas “muy bajo” o “muy alto” hasta acertar.
# Al final muestra el número secreto y cuántos intentos llevaste.

import random
# El número secreto se generará aleatoriamente entre estos límites.
MIN_NUM = 1
MAX_NUM = 100


# GENERAR NÚMERO SECRETO
# Se crea un número aleatorio que el usuario debe adivinar.
numero_secreto = random.randint(MIN_NUM, MAX_NUM)


# MENSAJE DE BIENVENIDA
print("🎮 ¡Bienvenidos a mi juego de adivinanza!")
print(f"Reglas: debes adivinar el número secreto entre {MIN_NUM} y {MAX_NUM}.")
print("Tip: el programa te dirá si tu número es 'muy bajo' o 'muy alto'.")
print("¡Buena suerte! ✨")

# CONTADOR DE INTENTOS
# Aquí se acumulan las veces que el usuario ingresa un número válido.
intentos = 0


# BUCLE PRINCIPAL DEL JUEGO
while True:
    entrada = input(f"\nIngresa un número ({MIN_NUM}-{MAX_NUM}): ").strip()

    # VALIDACIÓN: ¿Es un entero?
    # isdigit() solo da True si la entrada son dígitos (por ejemplo: "25").
    # Si el usuario escribe letras o decimales, no es válido.
    if not entrada.isdigit():
        print("❌ Error: ingresa un número entero válido (por ejemplo: 25).")
        continue  # volvemos a pedir otro número (el juego sigue)

    # Convertimos el texto a entero para poder compararlo.
    adivinanza = int(entrada)

    # Contamos el intento (solo después de pasar la validación del entero).
    intentos += 1

    
    # VALIDACIÓN: ¿Está en el rango?
    
    # Verificamos si el número está dentro de MIN_NUM y MAX_NUM.
    if adivinanza < MIN_NUM or adivinanza > MAX_NUM:
        print(f"⚠️ Fuera de rango. Debe estar entre {MIN_NUM} y {MAX_NUM}.")
        continue  # vuelve a pedir (el juego sigue)

    # COMPARACIÓN: PISTAS
    # Si el número del usuario es menor que el secreto, entonces está "muy bajo".
    if adivinanza < numero_secreto:
        print("📉 Muy bajo. Intenta con un número más alto.")
    # Si el número del usuario es mayor que el secreto, entonces está "muy alto".
    elif adivinanza > numero_secreto:
        print("📈 Muy alto. Intenta con un número más bajo.")
    # Si es exactamente igual, ¡acertaste!
    else:
        print(f"\n✅ ¡Correcto! Adivinaste el número {numero_secreto}.")
        # Mostramos cuántos intentos hizo el usuario.
        print(f"🏁 Te tomó {intentos} intento(s).")
        break  # termina el juego
