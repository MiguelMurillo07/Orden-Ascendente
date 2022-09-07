# Instrucciones Condicionales

##Caso No. 10: Dados 3 números devolverlos de forma ascendente


print("---------------------------------")
print("--------Orden Ascendente---------")
print("---------------------------------")

# input
a = int(input("Digite el valor del primer número: "))
b = int(input("Digite el valor del segundo número: "))
c = int(input("Digite el valor del tercer número: "))

# processing

print("El Orden Ascendente es asi:")
if(a>b and b>c):
    print("", a , " - ", b , " - ", c)
elif(b>a and a>c):
    print("", b , " - ", a , " - ", c)
elif(c>a and a>b):
    print("", c , " - ", a , " - ", b)
elif(a>c and c>b):
    print("", a , " - ", c , " - ", b)
elif(c>b and b>a):
    print("", c , " - ", b , " - ", a)
elif(b>c and c>a):
    print("", b , " - ", c , " - ", a)
else:
    print("Se digitaron números iguales.") 
    