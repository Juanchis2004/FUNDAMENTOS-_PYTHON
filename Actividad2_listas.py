
# Actividad 2: Análisis de Temperaturas Semanales

temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# 1) Imprime la lista completa de temperaturas
print("Temperatura del primer dia:", temperaturas[0])
print("Temperatura del ultimo dia:", temperaturas[-1])
print("Temperatura del dia 7 (mitad):", temperaturas[6])

# 3) Usa slicing para extraer e imprimir
semana1 = temperaturas[0:7]
semana2 = temperaturas[7:14]

pares_en_quincena = temperaturas[1:14:2]
print("\nprimera semana (dias 1-7):", semana1)
print("segunda semana (dias 8-14):", semana2)
print("Temperaturas de dias pares (2,4,6,...,14):", pares_en_quincena)
print("Temperaturas (quincena completa):", temperaturas)

# 4) Calcula e imprime el promedio de cada semana usando sum() y len() sobre los slices
promedio_semana1 = sum(semana1) / len(semana1)
promedio_semana2 = sum(semana2) / len(semana2)

print("\nPromedio semana 1:", promedio_semana1)
print("Promedio semana 2:", promedio_semana2)

# Determina cuál de las dos semanas tuvo mayor temperatura promedio y muestra un mensaje descriptivo
if promedio_semana1 > promedio_semana2:
    print("\nBonus: La semana 1 tuvo el mayor promedio de temperatura.")
elif promedio_semana2 > promedio_semana1:
    print("\nBonus: La semana 2 tuvo el mayor promedio de temperatura.")
else:
    print("\nBonus: Ambas semanas tuvieron el mismo promedio de temperatura.")
