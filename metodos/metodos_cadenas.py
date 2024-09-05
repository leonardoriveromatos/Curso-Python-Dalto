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

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena, len() es una funcion por lo que se le pasa la cadena que se quiere contar
contar_caracteres = len(cadena1)

#Verificar si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("h")

#Verificar si una cadena termina con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.endswith("la")

#reemplaza un pedazo de la cadena dada por otra
cadena_nueva = cadena1.replace("hola", "Hola leo" )

#Separar cadenas con la cadna que le pasemos
cadena_separada = cadena1.split(",")