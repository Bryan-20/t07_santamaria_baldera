# Ejercicio nro 03
# Ingrese a1 y luego pedir a2, mientras a2 sea menor a a1
# Donde a1 es un numero para entero positivo
a1=1
numero_ivalido=((a1%2)!=0)
a2=0
while(numero_ivalido):
    a1=int(input("Ingrese a1:"))
    numero_ivalido=((a1%2)!=0)
while(a2<a1):
    a2=int(input("Ingrese a2:"))
#Fi_While
print("A1=",a1,"A2=",a2)
