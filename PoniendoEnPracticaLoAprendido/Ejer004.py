# Programa que cuenta la longitud de una cadena de texto ingresada por el usuario

respuesta = input("Soy un contador de cadenas de texto pasame una frase y contare sus caracteres \n")

longitud = 0

for i in respuesta:
    longitud = longitud+1

print("Esta es la longitud de " + respuesta + "': " + str(longitud))
