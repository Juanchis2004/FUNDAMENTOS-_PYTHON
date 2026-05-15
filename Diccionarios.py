#Diccionarios (caracteristicas a un elemento)

#creacion de un diccionario

#estructura de un diccionario
diccionario={"clave1":"valor1", "clave2":"valor2", "clave3":"valor3"}

diccionario_aprendizes={"nombre":"juan", "apellido":"perez", "edad": 21, "programa":"python", "Ficha":3321349, "municipio":"Tibasosa"}

print(type(diccionario_aprendizes)) #<class 'dict'>
print(diccionario_aprendizes["nombre"]) #acceder a un valor del diccionario
print(diccionario_aprendizes["programa"]) #acceder a un valor del diccionario
print(diccionario_aprendizes["Ficha"]) #acceder a un valor del diccionario
print(diccionario_aprendizes["municipio"]) #acceder a un valor del diccionario
print(diccionario_aprendizes["correo"]) #acceder a un valor del diccionario
print(diccionario_aprendizes.keys()) #acceder a las claves del diccionario
print(diccionario_aprendizes.values()) #acceder a los valores del diccionario
print(diccionario_aprendizes.items()) #acceder a las claves y valores del diccionario

diccionario_aprendizes["correo"]="juansebastiangirataguarin12@gmail.com"

#modificar un valor del diccionario
diccionario_aprendizes["programa"]= "SST"
print(diccionario_aprendizes)

#metodo update()
diccionario_aprendizes.update({"nombre":"juan"})
diccionario_aprendizes.update({"municipio":"Tibasosa"})
diccionario_aprendizes.update({"edad": 21})
diccionario_aprendizes.update({"programa":"python"})

for ficha in diccionario_aprendizes:
    if ficha in diccionario_aprendizes:
        print(diccionario_aprendizes[ficha])
        
for clave in diccionario_aprendizes.keys():
    print(clave)
    
    #reccorer solo los valores del diccionario
for valor in diccionario_aprendizes.values():
    print(valor)
    
    
    aprendices = {
        "aprendiz_1":{
            "nombre":"juan",
            "apellido":"perez",
            "edad": 21,
            "programa":"python",
            "Ficha":3321349,
            "municipio":"Tibasosa"
        },
    "aprendiz_2":{
            "nombre":"maria",
            "apellido":"gomez",
            "edad": 20,
            "programa":"java",
            "Ficha":3321350,
            "municipio":"Duitama"
            
    },
    "aprendiz_3":{
            "nombre":"pedro",
            "apellido":"lopez",
            "edad": 22,
            "programa":"javascript",
            "Ficha":3321351,
            "municipio":"Tunja"
    }
    } 
    
    #acceder a un valor en un dicionario anidado
print(aprendices["aprendiz_1"]["nombre"]) #juan

#recorrer un diccionario anidado con un ciclo for
for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")   
    
        