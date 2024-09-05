lista = list({"hola", "leo", 24})

cadena = "hola"

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Agregando un elemento a la lista
lista.append("jsjjjaja")

#Agregando elemento a la lista con indice especifico
lista.insert(2, "Bienvenido")

#Agregando varios elementos a la lista
lista.extend([False, 2020])

#Eliminando un elemento de la lista por su indice
lista.pop(0)

#Eliminando un elemento de la lista por su indice de atras hacia adelante, con -1 elminia el ultimo, con -2 el antepenultimo y asi sucesivamente
lista.pop(-2)

#Removiendo elemento de la lista por su valor
lista.remove("Bienvenido")

#Eliminando todos los elementos de la lista
#lista.clear()

lista1 = list({232,334,23,2,343,False,True})

#Ordenando una lista numerida, de forma ascendente si usanmos el parametro (reverse = True) lo oedena en reversa
lista1.sort()

#Invirtiendo los elementos de una lista
lista1.reverse()