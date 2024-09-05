cadena1 = "Hola soy Leo"
cadena2 = "Bienvenido dev"

# dir es una funcion que devuelve la lista de atributos validos del objeto pasado, es decir
# todo lo que se puede hacer con el objeto que se pasa por parametros, varia en dependencia del tipo de valor

#print(dir(cadena1))


# Diferencia de funcion y metodo

#Metodo forma en que funcionan: dato.nombre del metodo()

# resultado = cadena1.upper()  upper esta funcionando como un metodo sobre la variable cadena1

# resultado = upper(cadena1)   upper en este caso esta siendo llamada como una funcion de python y dara error

# Upper convierte la cadena str a mayusculas
mayusculas = cadena1.upper()

 #lower converte la cadena str a minuscula
minusculas = cadena1.lower() 

#Convierte la primera letra en mayusculas
primera_letra_en_mayusculas = cadena1.capitalize()

#busca una cadena en otra cadena y devuelve la posicion en la que encuentra lo que se le pide y es sensible a mayusculas y minisculas
# y si no encuentra resultado devuelve -1   
busqueda_find = cadena1.find("hola")

#busca una cadena en otra cadena, mismo funcionamiento de find lo que esta sino encuentra coincidencia devuelve una excepcion
busqueda_index = cadena1.index("d")

#si es numerico devuelve true
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")

#

