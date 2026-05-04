print("Hola Mundo")
#Tipos de escritura de variabl
camelCase = "SENA"
aprendiz = "SENA"

nombre = " Sebastian"
apellido = "Giratá"
edad = 21
altura = 1.81
activo = True
correo = "sebastian.girata@sena.edu.co"

telefono_str = "3216549870"
cedula = 1055312061
telefono_int = int(telefono_str)
edad_float = float(edad)
altura_int = int(altura)
cedula_str = str(cedula)

print(type(nombre))
print(type(apellido))
print(type(edad))
print(type(altura))
print(type(activo))
print(type(correo))
print(type(telefono_str))
print(type(telefono_int))
print(telefono_int)
print(type(edad_float))
print(edad_float)
print(type(altura_int))
print(altura_int)
print(type(cedula_str))
print(cedula_str)


#identacion
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

#inputs
print("Ahora te voy a pedir un dato...")
nombre_completo = input("Ingrese su nombre completo: ")
print(f"Nombre completo: {nombre_completo}")

valor1= float(input("ingrese primer valor "))
valor2= float(input("ingrese segundo valor "))

print("elije la operacion")
print("1.suma \ 2.resta \ 3.multiplicacion \ 4.divicion \ 5.modulo \ 6.divicion_entero \ 7.potencia")

suma= float (valor1 +valor2)
resta= float(valor1-valor2)
multiplicacion= float(valor1*valor2)
divicion= float(valor1/valor2)
modulo= float(valor1%valor2)
divicion_entero= float(valor1//valor2)
potencia= float(valor1**valor2)

opcion= int(input("escoge una opcion (numero): "))


if  opcion==1 :
    print(suma)
elif opcion==2 :
    print(resta)
elif opcion==3:
    print(multiplicacion)
elif opcion==4 :
    print(divicion)
elif opcion==5 :
    print(modulo)
elif opcion==6:
    print(divicion_entero)
elif opcion==7:
    print(potencia)
else:
    print("opcion no valida")



