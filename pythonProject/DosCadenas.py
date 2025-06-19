##Ejemplo cadenas de caracteres

#String concatenar una cadena
'''
text1 = "Fundamenteos con "
text2 = "Python"
result = text1 + text2
print(result)
'''

#Format string
'''
price = 97
text3 = f"The price is {price:.2f} dollars"
#f tiene que ir al principio para concatenar el valor numero
#.2f es el numero de decimales que va a mostrar
print(text3)
'''

#Ejemplo
'''
#f es para darle formato a la cadena
firstname = "Jorge"
lastname = "Aguirre"
fullname = f"el nombre completo es {firstname} con {lastname}"
print(fullname)
'''

#Math operation
'''
text4 = f"la multiplicacion es: {20*59}"
print(text4)
'''


#Python integra un conjunto de metodos que se usan con las cadenas
#Ejemplo funcion capitalize()
#Pone en mayúscula la primer letra de una frase
#String capitalize
'''
text5 = "python es un lenguaje de alto nivel"
result1 = text5.capitalize()
print(result1)
'''


#Ejemplo función casefold()
#Convierte la cadena en minúscula, esta funcion es mas fuerte que lower()
#String casefold()
'''
title= "Cien Años de Soledad"
titleConvert = title.casefold()
print(titleConvert)
'''

#Ejemplo Funcio ncenter
#Agrega caracteres ocupando los espacios establecidos
#String center()
'''
fruit = "banana"
textCenter = fruit.center(20,"-")
print(textCenter)
'''

#Ejmeplo Funcion count()
#Devuelve el número de veces que aparece el valor en la cadena
#String count()
'''
title1 = "I love apple and apples are my favorite fruit"
result2 = title1.count("apple")
print(result2)
'''

#Ejemlplo funcion endswith()
#Funcion que comprueba si la cadena termina con un signo de puntuación
#String endswith
'''
text6 ="Curso, fundamenteos con python."
result3 = text6.endswith(".")
print(result3)
'''


#Ejemplo funcion expandtabs()
#La funcion establece el tamaño de tabulaciones en la cantidad especificadas de espacios en blanco
#String expandtabs()
'''
letter ="F\tU\tP"
letterSpaces = letter.expandtabs(1)
print(letterSpaces)
'''

#Ejemplo funcion find()
#Esta funcion encuentra la primera aparición del valor especificado
#String find
'''
text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(result4)
'''
#Ejemplo funcion title()
#Esta funcion escribe en mayuscula la primera letra de cada palabra
#Funcion title
'''
text8 = "welcome to my world"
result5 = text8.title()
print(result5)
'''

#Ejemplo función isalnum()
#Esta funcion deveulve Verdadeor si todos los caracteres de la cedna son alfanumercios
#Funcion isalnum
'''
alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)
'''
#Ejemplo isalpha()
#Esta funcion devuelve Verdadero si a todos los caracteres de la cadena estan en el alfabeto
#Funcion isalpha
'''
letters = "Space X"
result7 = letters.isalpha()
print(result7)
'''


