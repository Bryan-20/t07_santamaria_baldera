#Ejercicio nro 01
# pedir una nota de matematicas, donde la nota debe estar entre 0 y 20
# mientras la nota ingresada no es valida debe ingresarce otra vez.
nota=int (input("ingrese nota:"))
while(nota < 0  or nota >20):
    nota=int(input("Ingrese nota"))
#fin_While
print("La nota es:",nota)

nota=-1
nota_invalida=(nota < 0 or nota > 20)
while(nota_invalida):
    nota=int (input("ingrese nota(0-20):"))
    nota_invalida
    lida=(nota < 0 or nota > 20)
# Fin_while
