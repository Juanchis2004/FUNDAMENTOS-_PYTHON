conjunto={}
print(type(conjunto)) #<class 'dict'>

#------creacion-----
lenguajes_programacion={"python", "java", "c++", "javascript"}
print(lenguajes_programacion)


# --- Métodosde modificación ---
frutas = {"mango", "guayaba", "mora"}
frutas.add("maracuya")
frutas.add("mango")
frutas.remove("mora")
frutas.discard("papaya")
elem=frutas.pop()
print(frutas)

# ---verificar pertenencia: 0(1)---
print("python" in lenguajes_programacion) #True
print("COBOL" in lenguajes_programacion) #False

python_devs ={"Ana", "Luis", "Maria", "Pedro"}
java_devs = {"Luis", "Carlos", "Sofia", "Marta"}

#
#UNION | :todos los elementos de ambos conjuntos sin duplicados
todos = python_devs | java_devs
# o tambien:python_devs.intersect(java_devs)
print("interseccion:", todos) #{'Luis', 'Carlos'}}


#diferencia - : los que A que no estan en B
solo_python = python_devs - java_devs
# o tambien: python_devs.difference(java_devs)
print("solo python:", solo_python) #{'Ana', 'Marta', 'sofia'}

solo_java = java_devs - python_devs
print("solo java:", solo_java) #{'pedro', 'Laura'}


#DIFERENCIA SIMETRICA ^ : los que estan en uno pero no en ambos
exclusivos = python_devs ^ java_devs
# o tambien: python_devs.symmetric_difference(java_devs)
print("exclusivos:", exclusivos) #{'Ana', 'Marta', 'Sofia
#{'Ana', 'Marta', 'Sofia', 'Pedro', 'Laura'}




#