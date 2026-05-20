# Diccionarios - Sistema de Registro de Aprendices

def calcular_promedio(lista_notas):
    return sum(lista_notas) / len(lista_notas)

# Diccionario principal: la clave es la ficha (int)
grupo = {
    3321349: {
        "nombre": "Juan",
        "edad": 21,
        "notas": [4.0, 3.8, 4.5],
        "ciudad": "Tibasosa"
    },
    3321350: {
        "nombre": "Maria",
        "edad": 20,
        "notas": [2.5, 3.0, 2.8],
        "ciudad": "Duitama"
    },
    3321351: {
        "nombre": "Pedro",
        "edad": 22,
        "notas": [3.2, 3.4, 3.6],
        "ciudad": "Tunja"
    },
    3321352: {
        "nombre": "Laura",
        "edad": 19,
        "notas": [4.8, 4.2, 4.6],
        "ciudad": "Paipa"
    }
}

print("REPORTE DE APRENDICES")
print("-" * 60)

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos["notas"])
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    
    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Promedio: {promedio:.1f}")
    print(f"Estado: {estado}")
    print("-" * 60)

# Agregar un nuevo aprendiz
grupo[3321353] = {
    "nombre": "Carlos",
    "edad": 23,
    "notas": [3.5, 3.7, 3.9],
    "ciudad": "Sogamoso"
}

# Actualizar la ciudad de uno de los aprendices
grupo[3321350]["ciudad"] = "Nueva Ciudad"

print("\nREPORTE ACTUALIZADO")
print("-" * 60)

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos["notas"])
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    
    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Promedio: {promedio:.1f}")
    print(f"Estado: {estado}")
    print("-" * 60)

# Bonus: ordenar de mayor a menor promedio
print("\nLISTA ORDENADA POR PROMEDIO")
print("-" * 60)

ordenados = sorted(grupo.items(), key=lambda item: calcular_promedio(item[1]["notas"]), reverse=True)

for ficha, datos in ordenados:
    promedio = calcular_promedio(datos["notas"])
    print(f"{datos['nombre']} - Ficha {ficha} - Promedio: {promedio:.1f}")

# Ejercicio adicional
print("\nEJERCICIO 1")
vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)
producto_escalar = sum(a * b for a, b in zip(vector1, vector2))
print("Producto escalar:", producto_escalar)

print("\nEJERCICIO 2")
precios = [50, 75, 46, 22, 80, 65, 8]
menor_precio = min(precios)
mayor_precio = max(precios)
print("Menor precio:", menor_precio)
print("Mayor precio:", mayor_precio)
