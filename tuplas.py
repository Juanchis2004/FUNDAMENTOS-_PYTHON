#estructura de una tupla

tupla=("elemnyo 1", "elemnto 2", "elemento 3")

print(type(tupla))

tupla_2= "e", "r", "y"
print(type(tupla_2)) #<class 'tuple'>



tupla_3= ("hola")
print(tupla_3) #si la tupla no tiene "," lo registr como otro tipo de dato

tupla_4=tuple("hola")  #si agregamos esta funcion, hace que la palabra sea un eleemnto por aparte
print(tupla_4) #= ('h', 'o', 'l','a')

tupla_mixta=("gol", 43, True)
print(tupla_mixta)

aprendices= ("juan", "maria", "pedro")
print(aprendices[1]) #acceder a un elemento de la tupla,

print(aprendices.index("maria")) #acceder a un elemento de la tupla, pero con su indice

#modificar una tupla en una lista

print(type(aprendices)) #<class 'tuple'>
aprendices_lista=list(aprendices) #convertir la tupla en una lista
print(type(aprendices_lista)) #<class 'list'>
aprendices_lista.append("juan") #agregar un elemento a la lista
print(aprendices_lista)

aprendices=tuple(aprendices_lista) #convertir la lista en una tupla
print(aprendices)

#Ejercicio 2 desempaquetar tuplas
tupla_ciudades= ("medellin", "bogota", "cali")
ciudad_1, ciudad_2, ciudad_3= tupla_ciudades
print(ciudad_1)
