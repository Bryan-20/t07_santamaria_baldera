# Ejercicio nro 02
# Mostrar "Intruso" Mientras la clave no sea abc1234.
password=""
password_ivalid=(password!="abc123")
while(password_ivalid):
    print("Intruso")
    password=input("Enter password:")
    password_ivalid=(password!="abc1234")
#fin_while
print("Welcome")
