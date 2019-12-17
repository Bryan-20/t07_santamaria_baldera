# #Ejercicio nro 04
#Pedir la edad de una persona mientras la edad sea valida don la edad
# no puede ser negativa ni mayor a 60
edad=0
edad_inv=(edad < 18 or edad >60)
while(edad_inv):
    edad=int(input("Ingrese Edad:"))
    edad_inv=(edad < 18 or edad > 60)
#Fin_while
print("Edad valida",edad)
