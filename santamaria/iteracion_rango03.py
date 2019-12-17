# Ingrese el cantidad de empleados, donde el sueldo < 500 y pedir el total a pagar
suma=0
cont1=0
cont2=0
n=int(input("Ingrese cantidad de empleados:"))
for i in range(1,n+1):
    sueldo=float(input("Ingrese sueldo:"))
    suma+=sueldo
    if(sueldo<500):
        cont1+=1
    #Fin_if
#Fin_ford
    else:
        cont2+=1
print("Menos de 500:",cont1)
print("Mas de 500:",cont2)
print("Total en pagar:",suma)
