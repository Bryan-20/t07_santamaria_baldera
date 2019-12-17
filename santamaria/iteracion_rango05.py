# Ejerecicio nro 05
# Introducir dos numeros donde la suma de sus resultados sean perfectas
num1=int(input("Introduce un numero:"))
num2=int(input("Introduce un numero:"))

for i in range(num1,num2+1):
    suma=0
    for j in range(1,(i//2)+1):
        if(i%j==0):
            suma+=j
    if(suma==i):
    #Fin_if
#Fin_For
        print("El numero",i," es perfecto porque la suma es:",suma)
