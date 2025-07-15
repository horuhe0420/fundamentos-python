#Condición Simple
#Solo evalua una condicion, si es verdadera hace algo sino nada

#Simple
'''
a=33
b=200
if b>a:
    print(f"{b} es mayor que {a}")
'''
#Doble
'''
a=200
b=333
if a>b:
    print(f"{b} es mayor que {a}")
else:
    print(f"{b} no es mayor que {a}")
'''

#Multiple
'''
a=200
b=207
if a>b:
    print(f"{a} es mayor que {b}")
elif a<b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual que {b}")
'''
#Condiciones enlazadas
'''
x=28
if x>10:
    print("por encima de diez")
    if x>20:
        print("y también por encima de 20!")
    else:
        print("pero no por encima de 20")
'''

#PARAMETROS END Y SEP
#end con espaico vacio evita que haga el enter por defecto
'''
print("Estudiar los sabados", end=' ')
print("es genial")

#print("Estudiar los sabados", end='')
#print("es genial")
#PARAMETRO SEP
print("Daniela","luis","Carlos","Camila") #Agrega espacio por defecto
print("Daniela","luis","Carlos","Camila", sep="") #Quita el espacio
print("Daniela","luis","Carlos","Camila",sep=",") #Agrega una coma

print("Daniela","luis","Carlos","Camila",sep="_", end="_Curso_Python")
'''
#CASO DE ESTUDIO
'''
"IN-N-OUT BURGER" ofrece hamburguesas secillas, dobles y triples, las cuales
tienen un costo de 20k,25k y 28k respectivamente. La empresa acepta
tarjetas de credito cn un cargo de 7%, otros medios de pago 0%, sobre la compra.
Suponiendo que los clientes adquieren solo un tipo de hamburguesa,
realice un programa para determinar cuanto debe pagar una persona por N
hamburguesas
'''
# Definir constantes
PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07

# Proceso
# Función para calcular el precio
def calcular_precio(tipo_hamburguesa, medio_pago, cantidad):
    # Definir precios según el tipo de hamburguesa
    if tipo_hamburguesa == 1:
        precio = PRECIO_SENCILLA
        descripcion = "Sencilla"
    elif tipo_hamburguesa == 2:
        precio = PRECIO_DOBLE
        descripcion = "Doble"
    elif tipo_hamburguesa == 3:
        precio = PRECIO_TRIPLE
        descripcion = "Triple"
    else:
        return None  # Tipo de hamburguesa inválido

    # Calcular el total sin cargos
    total_sin_cargo = precio * cantidad

    # Aplicar impuesto si el medio de pago es tarjeta
    if medio_pago == 1:
      impuesto = round(total_sin_cargo * IMPUESTO_TARJETA)
    else:
      impuesto = 0

    total = round(total_sin_cargo + impuesto)

    # Retornar datos relevantes
    return descripcion, precio, cantidad, impuesto, total

# Función para generar mensaje
def generar_mensaje(descripcion, precio, cantidad, impuesto, total):
    return (f"Tipo de Hamburguesa: {descripcion}\n"
            f"Precio: ${precio}\n"
            f"Cantidad: {cantidad}\n"
            f"Impuesto: ${impuesto}\n"
            f"Total: ${total}")

# Función para validar los datos
def validar_datos(tipo_hamburguesa, medio_pago, cantidad):
    if 1 <= tipo_hamburguesa <= 3 and 1 <= medio_pago <= 2 and cantidad > 0:
        resultado = calcular_precio(tipo_hamburguesa, medio_pago, cantidad)
        #print("Resultado: ",resultado)
        descripcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje(descripcion, precio, cantidad, impuesto, total)
        print("--------------------------\n" + mensaje)
    else:
        print("Verifique las opciones ingresadas.")

# Entradas
tipo_hamburguesa = int(input("Tipos de hamburguesa \n1. Sencilla \n2. Doble \n3. Triple \nIngrese una opcion: "))
medio_pago = int(input("Medios de pago \n1. Tarjeta \n2. Otro \nIngrese una opcion: "))
cantidad = int(input("Ingrese la cantidad: "))

# Salidas
validar_datos(tipo_hamburguesa, medio_pago, cantidad)