frase = input("Dime una frase para calcular el tiempo que demorarias en decirla: ")
palabras_separadas = frase.split()
cantidad_de_palabras = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabras} palabras y te tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras/2 * 0.3} segundos")
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")