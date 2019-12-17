# Ejercicio 01
n=0
while(n<501):
    print(n)
    n=n+1
#fin_while

# Ejercicio 02
n=0
while(n<403):
    print(n)
    n=n+3
#fin_while

# Ejercicio 03
n=1
while(n<700):
    print(n)
    n=n*2
#fin_while

# Ejercicio 04
n=1
while(n<500):
    print(n)
    n=n*5
#fin_while

# Ejercicio 05
n=1
while(n<1003):
    print(n)
    n=n+3
#fin_while


# Ejerecicio Mientras 01
#Pedir la edad de una persona mientras la edad sea valida, donde la edad no puede ser negativo ni mayor a 80
edad=0
edad_inv=(edad<20 or edad >80)
while(edad_inv):
    edad=int(input("Ingrese Edad:"))
    edad_inv=(edad<20 or edad >80)
#fin_while
print("Edad valida",edad)

# Ejerecicio Mientras 02
#Pedir la edad de una persona mientras la edad sea valida don la edad no puede ser negativo ni mayor a 60
edad=0
edad_inv=(edad<25 or edad >70)
while(edad_inv):
    edad=int(input("Ingrese Edad:"))
    edad_inv=(edad<25 or edad >70)
#fin_while
print("Edad valida",edad)

# Ejerecicio Mientras 03
#Pedir la nota de un alumno mientras la nota sea aprobada don la nota no puede menor de 10.5 ni mayor a 20
nota=0.0
nota_desaprobada=(nota<10.5 or nota >20)
while(nota_desaprobada):
    nota=float(input("Ingrese Nota:"))
    nota_desaprobada=(nota<25 or nota >70)
#fin_while
print("Nota desaprobada",nota)

# Ejerecicio Mientras 04
#Pedir el peso de un adulto mientras el peso sea normal don el peso no puede ser menor de 30 ni mayor a 90
peso=0
peso_elevado=(peso<30 or peso >90)
while(peso_elevado):
    peso=int(input("Ingrese Peso:"))
    peso_elevado=(peso<30 or peso >90)
#fin_while
print("Peso Elevado",peso)

# Ejerecicio Mientras 05
#Pedir la edad de una persona mientras la edad sea valida don la edad no puede ser negativo ni mayor a 60
edad=0
edad_inv=(edad<40 or edad >80)
while(edad_inv):
    edad=int(input("Ingrese Edad:"))
    edad_inv=(edad<40 or edad >80)
#fin_while
print("Edad valida",edad)

# Codificadores 01
import os
msg=str(os.sys.argv[1])

for letra in msg:
    if(letra == "A"):
        print("AMOR")
    if(letra == "B"):
        print("BELLEZA")
    if(letra == "C"):
        print("CARRO")
    #Fin_if
#Fin_For


# Codificadores 02
import os
msg=str(os.sys.argv[1])

for letra in msg:
    if(letra == "D"):
        print("DADO")
    if(letra == "E"):
        print("ELEGANCIA")
    if(letra == "F"):
        print("FIERRO")
    #fin_if
#Fin_For

# Codificadores 03
import os
msg=str(os.sys.argv[1])

for letra in msg:
    if(letra == "G"):
        print("GATO")
    if(letra == "H"):
        print("HILO")
    if(letra == "I"):
        print("IMAN")
    #Fin_If
#Fin_For


# Codificadores 04
import os
msg=str(os.sys.argv[1])

for letra in msg:
    if(letra == "F"):
        print("FELIZ")
    if(letra == "C"):
        print("CUMPLEAÑOS")
    if(letra == "J"):
        print("JORGUE")
    #Fin_if
#Fin_For


# Codificadores 05
import os
msg=str(os.sys.argv[1])

for letra in msg:
    if(letra == "F"):
        print("FELICES")
    if(letra == "F"):
        print("FIESTAS")
    if(letra == "P"):
        print("PATRIAS")
    #Fin_if
#Fin_For

#Ejercicio iterecion 01
#Ingresar 10 numeros y luego pedir la suma y la media de los numeros ingresados
lista=[]
suma=0
media=0
numero=0
for i in range(10):
    numero=float(input("Dame un numero:"))
    lista.append(numero)
    suma+numero
#fin_for
print("Los numeros son:")
for i in lista:
    print(i)
#fin_for
media_=suma/len(lista)
print("La suma es",suma)
print("La media es",media)


#Ejercicio iterecion 02
#Ingresar 20 numeros y luego pedir la suma y la media de los numeros ingresados
lista=[]
suma=0
media=0
numero=0
for i in range(20):
    numero=float(input("Dame un numero:"))
    lista.append(numero)
    suma+numero
#fin_for
print("Los numeros son:")
for i in lista:
    print(i)
#fin_for
media_=suma/len(lista)
print("La suma es",suma)
print("La media es",media)
