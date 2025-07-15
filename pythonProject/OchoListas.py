#Definición de una lista
#Son mutables
'''
lista = []
lista1 = ["Esto es un texto"]
lista2 = ['una cadena', 123]
lista3 = [1,2,3,4.5,'hola','a']
print(lista)
print(lista1)
print(lista2)
print(lista3)
'''
#Listas enlazadas
'''
lista5 = [0,1,2,3]
lista6 = ["A","B","C"]
lista7 = [lista5,lista6]
print(lista7)
print(lista7[0])#Muestra sola lista5
print(lista7[7])#Muestra sola lista6
print(lista7[1][0])#Muestra solo 
'''
#Concatenacion
'''
lista8 = ["A","B","C","D"]
lista9 = [1,2,3,4,5]
lista10 = lista8 + lista9

nom1 = ["Antonio", "Maria"]
nom2 = ["Barry","John"]
nom1.extend(nom2)
print(nom1)
print(nom2)

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
#Extender l1 con los elemtnos de l2 y l3
l1.extend(l2)
l1.extend(l3)

print(l1)
'''
#Operciones con listas
#Es posible determinar si un lemento se encuentra en la lista
'''
lista13 = ["cien","años","de","soledad"]
if "de" in lista13:
    print("Si esta en la lista")
else:
    print("No esta en la lista")
'''
#Iterando una lista
'''
lista15 = ["cien","años","de","soledad"]
for palabra in lista15:
    print(palabra, end=",")
'''
