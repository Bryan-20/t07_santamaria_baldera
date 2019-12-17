# Ingrese un contador con un  rango de 100 a 700  y pedir la cantidad de multiplos de 3 y 7
contador=0
for i in range(100,700):
    if(i%3==0 and i%7==0):
        contador+=1
    #Fin_si
#fin_for
        print(i)
print("La cantidad de multiplos de 3 y 7 es:",contador)
