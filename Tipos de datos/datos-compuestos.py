#Creando una lista (Se pueden modificar)
lista = ["Leo", "Hola", True,1.73]#Tipo de dato lista

#Esto es valido
lista[3] = "Holaaaaaaa"

#Creando una lista (No se pueden modificar)
tupla = ("Leo", "Hola", True,1.73)#Las tuplas son lo mismo que una lista solo que estas no se pueden modificar

#Esto no es valido
#tupla[3] = "Holaaaaaaaaaa"

#Creando un conjunto (set)
#En un conjunto no pueden haber datos duplicados y no se pueden acceder a los elementos por su indice
#Son datos desordenados
conjunto = {"Leonardo Matos","Holaaaaaaaa",True,1.73}

#Creando un diccionario (Es literalmente un json)
diccionario = {
    'nombre' : "Leonardo",
    'apellido': "Rivero",
    'esta_emocionado' : True,
    'altura' : 1.73,
    'dato_duplicado' : "Rivero",
}

print(diccionario['altura'])
