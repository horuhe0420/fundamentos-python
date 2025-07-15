#Primitivamente existen:
#while y for
#Mientras - While

#Ejmeplo1
'''
i=0
while(i <= 6):
    print(i)
    i = i +1 #i += 1
'''
#Ejmeplo2
'''
i=2
j=25
while i<j :
    print(i,j,sep=",")
    i *=2
    j += 10
print("the end")
print(i,j,sep=",")
'''
#Ejemplo3
'''
bandera = True
while bandera == True:
    op = input("¿Hay items para la lista S/N?")
    if op == "S" or op == "s":
        print("Si hay items")
    elif op == "N" or op == "n":
        print("No hay items")
        bandera = False
    else:
        print("Valor no valido!")
'''
#Ejemplo Menu
#Menu con opcion para calcular area triangulo, cuadrado, numeor spositvo negativo cero
'''
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

def calcularAreaCuadrado(l):
    area = l*l
    return area

salir = True

while salir == True:
    opcion = int(input("Ingrese una opción: \n1. Area Triangulo \n2. Area Cuadradoo \n4. Salir\n"))
    if opcion ==1:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        res = calcularAreaTriangulo(base,altura)
        print("Area Triangulo", res)
    elif opcion == 2:
        lado = int(input("Ingrese el lado: "))
        res = calcularAreaCuadrado(lado)
        print(f"Area del cuadrado: {res}")
        #pass
    elif opcion == 4:
        print("Hasta luego")
        salir = False
    else:
        print("Opcion no valida")
'''
#----------------FOR-----------------------------
#EJEMPLO 1
# ek ciclo for no requiere ua variable de indexacion praa establecere de antemanno
'''
frutas = ["manzana","banano", "pera"]
for x in frutas:
    print(x)
'''
#EJRMPLO 2
'''
for x in "Curso python":
    print(x, end=" ")
'''
#EJEMPLO 3
'''
nombres = ["Luis", "Juan", "Daniela"]
for x in nombres:
    print(x)
    if x == "Juan":
        break
'''
#EJEMPLO 5
'''
for x in range(7):
    print(x)
'''
#EJEMPLO 6
'''
for x in range(2,6): # la funcion range recibe 3 parametros, el tercero es el incrememto
    print(x)
'''
#EJEMPLO 7
'''
for x in range(2,20,2):
    print(x)
'''
#EJEMPLO 8 for anidado
# el bucle interno se ejecutará una ve por cada iteracion del buclo externo
adjetivo = ["rojo","grande","sabrosa"]
fruits = ["manzana", "banano", "fresa"]

for x in fruits:
    for y in adjetivo:
        print(x, y , sep='->')

#declaracion de pass
for x in [0,1,2]:
    pass