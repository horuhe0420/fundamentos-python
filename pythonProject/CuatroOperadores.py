#Operadores de asignación
#Para asignar valores a las variables
#= += -= *= /=
#Asignacion
'''
var1 = 5
var2 = 12
var3 = 8
var4 = 14
var5 = 6
var6 = 8

var1 += 3 #var1 = var1+3 Asignacion con suma
var2 -= 3 #var2 = var2-3 Asignacion con resta
var3 *= 3 #var3 = var3+3 Asignacion con mult
var4 /= 3 #var4 = var4+3 Asignacion con div
var5 %= 3 #var5 = var5+3 Asignacion con div mod
var6 //= 3 #var6 = var6+3 Asignacion con div entera

print(var1)
'''

#Op Aritemeticos + - * / % ** //
'''
num1 = 18
num2 = 12
s= num1 + num2
r= num1 - num2
d= num1/num2
m= num1 *num2
mod = num1 % num2
divEntera =num1 // num2

print(f"Suma: {s}")
print(f"Resta: {r}")
print(f"Multiplicacion: {m}")
print(f"Division  {d}")
print(f"Division Modular: {mod}")
print(f"Division Entera:  {divEntera}")
'''
#Operadores Comparación
'''
m= 45
n=23
print(m == n) #Igualdad
print(m > n)
print(m < n)
print(m >= n)
print(m <= n)
print(m != n)#No igual !
'''

#Comparadores lógicos
'''
#and(y)
q=5
print(q>4 and q<9)

#or (o)
print(q>5 or q<10)

#not (o)
print(not(q>2 and q<7))
'''
#Precedencia de operadores
'''
#Expresion 42//6+7*3-39
res0 = 42//6+7*3-39
res1 = (42//6)+7*3-39 #// Prioridad 3
res2 = (42//6)+(7*3)-39 #* Prioridad 3
res3 = ((42//6)+(7*3))-39 #+ Prioridad 4
res4 = (((42//6)+(7*3))-39) #- Prioridad 4
print(res4)
'''

#ESTRUCTURAS SELECTIVAS

