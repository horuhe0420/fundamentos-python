#Ejemplo
diccionario = {}
#Diccionario con 4 items o registros
puertos ={
    22:"SSH",
    23:"Telnet",
    80:"HTTP",
    3306:"MySQL"
}
print(puertos)

puertos1 ={
    22:"SSH",
    80:"HTTP"
}

puertos2 ={
    53:"DNS",
    443:"https"
}

print(puertos1)
puertos1.update(puertos2)
print(puertos1)

#Accediendo al valor de un item con la clave dada
puertos3 ={
    22:"SSH",
    23:"Telnet",
    80:"HTTP",
    3306:"MySQL"
}

protocolo = puertos3[22]
print(protocolo)

#Eliminar item con la clave dada
calificaciones = {
    "alumno1":5,
    "alumno2":3,
    "alumno3":4,
    "alumno4":3,
}

print(calificaciones)
del calificaciones["alumno3"]
print(calificaciones)

#Iterar un diccionario
#usar el ciclo for y el metodo items para obtener los items de un diccionario
dicPuertos = {
    22:"SSH",
    23:"Telnet",
    80:"Http"
}

for x,y in dicPuertos.items():
    print(x, "->", y)