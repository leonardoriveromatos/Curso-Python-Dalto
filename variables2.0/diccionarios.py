#Creando diccinarios con dict()
diccionario = dict(nombre = "Leo", apellido = "Rivero")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["nombre","apellidos"]): "Leo Rivero"}


#Creando diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")


#Creando diccionario con fromkeys() con dos parametros
diccionario = dict.fromkeys("ABCDE", "Algun valor fijo")
print(diccionario)