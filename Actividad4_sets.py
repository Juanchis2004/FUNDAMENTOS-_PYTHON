# Actividad 4 - Sets: Analisis de Matriculas del Centro de Formacion Adso

python_curso = {"Ana", "Luis", "Marta", "Carlos", "Sofia", "Pedro"}
java_curso = {"Luis", "Carlos", "Pedro", "Laura", "Diego"}
bd_curso = {"Marta", "Sofia", "Laura", "Ana", "Miguel", "Pedro"}

# 1. Total de aprendices unicos en los tres programas
unicos_tres = python_curso | java_curso | bd_curso
print("Aprendices unicos en los tres programas:", len(unicos_tres))
print(unicos_tres)

# 2. Aprendices que cursan Python y Java al mismo tiempo
python_y_java = python_curso & java_curso
print("\nAprendices en Python y Java:", python_y_java)

# 3. Aprendices que solo estan en Python
solo_python = python_curso - java_curso - bd_curso
print("\nAprendices solo en Python:", solo_python)

# 4. Aprendices en exactamente dos programas
exactamente_dos = ((python_curso & java_curso) - bd_curso) | ((python_curso & bd_curso) - java_curso) | ((java_curso & bd_curso) - python_curso)
print("\nAprendices en exactamente dos programas:", exactamente_dos)

# 5.Lista de inscripciones con duplicados
inscripciones = ["Ana", "Luis", "Ana", "Marta", "Carlos", "Luis", "Sofia", "Pedro", "Ana"]
unicos_inscripciones = set(inscripciones)

print("\nAprendices unicos inscritos:", len(unicos_inscripciones))
print(unicos_inscripciones)

# 6. Diccionario con el numero de programas por aprendiz
todos = python_curso | java_curso | bd_curso
conteo_programas = {
    aprendiz: sum([
        aprendiz in python_curso,
        aprendiz in java_curso,
        aprendiz in bd_curso
    ])
    for aprendiz in todos
}

print("\nCantidad de programas por aprendiz:")
print(conteo_programas)

# 7. Bonus: quien esta en los tres programas
en_tres = python_curso & java_curso & bd_curso
print("\nAprendices matriculados en los tres programas:", en_tres)
