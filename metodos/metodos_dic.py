diccionario = {
    "nombre" : 'leo',
    "apellido" : 'rivero',
    "edad" : 24
}

#nos devuelve un objeto dic_item
claves = diccionario.keys()

#Obteniendo un elemeto con get() (si no encuentra nada el progama continua)
valor_de_nombre = diccionario.get("nombre")

#Eliminando todo del diccionario
#diccionario.clear()

#Eliminando un elemento del diccionario
diccionario.pop("nombre")

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()


