#Son inmutables
'''
tupla1 = ()
print(tupla1)
tupla2 = ("Esto es un texto",)
print(tupla2)
tupla3 = ("Una cadena",123)
print(tupla3)
tupla4 = ("apple",2018,"samsung",4.9,"t",True)
print(tupla4)
'''
#ELEMENTOS DE UNA TUPLA
#print(tupla4[1])#Imprimo un elemento de acuerdo a la posicion
#Ejemplo 2
'''
tupla5 = (0,1,2,3)
tupla6 = ("A","B","C")
tupla7 = (tupla5,tupla6)
print(tupla7)
print(tupla7[0])#Muestra solo la tupla1
print(tupla7[1])#Muestra solo la tupla2
print(tupla7[1][0])#Muestra solo la tupla2 el elemento en el indice 0
'''
#CONCATENAR
'''
tupla8 = ("A","B","C","D")
tupla9 = (1,2,3,4.5)
tupla10 = tupla8 + tupla9
print(tupla10)
'''
#Repetir
#Crea una tupla con muktiples copias de una tupla
'''
tupla11 = (1,2,3,4.5)
tupla12 = tupla11 *3
print(tupla12)
'''
#Comparar
#Se usan los operadores convencionales (<,<=.>0,==,!=)
tupla13 = ("Rojas",)
tupla14 = (123,)
tupla15 = ("Rosas",)
tupla16 = ("rosas",)
print((tupla13, tupla14) < (tupla15,tupla14))
print((tupla15,tupla14) == (tupla16,tupla14))