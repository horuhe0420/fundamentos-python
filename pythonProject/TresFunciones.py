#Funciones
#Ejemplo funciones
'''
def my_function(): #Palabra reservada def, nombre de la funcion, paso de parámetros
    print("Hello from my function")
#Las funciones deben colocarse en forma de verbo
#Invocacion
my_function()
'''
#Función ocn argumentos
#Se coloca entre las funciones. Puede agregar tanto argumentos como desee, simplemente separarlso con coma

#Definir función
'''
def mostrar_Nombre(nombre):
    print("su nombre es "+ nombre)


mostrar_Nombre("Daniela")
'''
#Ejemplo calculo de area triangulo
'''
def calcualr_Area(b,h):
    ar = (b * h) / 2
    print("El area es: ")
    print(ar)


calcualr_Area(5,2)
'''
#Forma dos
'''
bas : int = 7
hig : int = 4
def calcular_Area(bas,hig):
    ar = (bas * hig) / 2
    #return ar
    result = calcular_Area(bas, hig)
    print("El area es:", result)
    text1 = f"The result is: {result}"
#Invocamos la función
calcular_Area()
'''

#Entradas por teclado
'''
base = input("Ingrese la base: ") #Es necesario hacer parsing, porque los datos entran como strings
altura = input("Ingrese la base: ")
'''
'''
base = float(input("Ingrese la base: ") )
altura = float(input("Ingrese la base: "))

def Area_C(base, altura):
    area = (base*altura)/2
    res = f"El area es: {area}"
    print(res)

Area_C(base, altura)
'''
#Argumento predeterminado
#Muestra un valor de un parámetro predeterminado
'''
def my_function2(country = "Colombia"):
    print("I am from  "+ country)

my_function2("Sweden")
my_function2()
'''
#Argumento arbitrario *args
#permite pasar un número indeterminado de argumentos de las funciones, de esta manera,
#la función recibirá una tupla de argumentos
'''
def mostrar_Estudiantes(*args):
    text = f"El nombre es: {args[1]}"
    print("El estudiante: "+ args[2])
    print(text)

mostrar_Estudiantes("Emil","Tobias", "Linus")
'''

#Argumentos de palabra clave
#clave = valor
'''
def mostrar_Carros(carro1, carro2, carro3):
    car = f"El carro es: {carro2}"
    print(car)

mostrar_Carros(carro1="BMW",carro3="Ferrari", carro2="Ford")
'''
#Argumento arbitrario **kwargs
#la función puede recibir un diccionario de argumentos (clave=valor)
'''
def mostrar_Carros2(**kwargs):
    car = f"El carro es: {kwargs["carro3"]}"
    print(car)

mostrar_Carros2(carro1="BMW",carro3="Ferrari", carro2="Ford")
'''

#Declaración de paso
#Se utiliza cmo marcador de posicion para futuras implementaciones de fucniones
def my_function():
    pass

#Funciones integradas
#Funciones matemiaticas integradas , incluido un extenso módulo matematico,
#que permiten relaizar tareas matematicas con numeros

#las funciones min() y max()
x = min(5,10,25)
y = max(5,10,25)


#Módulo matematicas
#Ejemplo math.sqrt()

import math
num2 = math.sqrt(34)
print(num2)

num3 = math.ceil(7.8)#redondeo por arriba
num4 = math.floor(7.8)#redondeo por abajo

print(num3)
print(num4)