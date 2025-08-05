print ("hola")

"""""
float numero =3.14
doble numero = 3.1489

#enteros int 
#booleanos bool
#string
tipos de condicionales 
if
elif
else
casos -> con las versiones de la ventana 3.10
ojo con  las versiones de python, por que las versiones inferiores no son compatibles con alguna sintaxis de versiones superiores 

ciclos ciclicos => de repeticion
for = para 
while = mientras 
break = romper # palabras reservadas 
continue = continuar #palabras resevadas en python 
pass = no hacer nada
"""""

#condicional simple
if True:
    print ("sxs mano")

edad = 18 
if edad >= 18 :
    print("Eres mayor de edad")
else:
    print("Eres un pelaito") 

    #condicionales anidados o multiples 
print ("Segun el numero es el rol que se va a mostrar") 
opcion = int(input("ingrese el numero de opcion: "))
if opcion == 1:
    print ("opcion 1 administrador")
elif opcion ==2:
    print("opcion 2 usuario")
elif opcion ==3:
    print ("opcion 3 aprendiz")
else:
    print ("opcion no valida")

print ("Segun el numero es el rol que se va a mostrar")
opcion = int(input("ingrese el numero de opcion: "))

match opcion:
    case 1: 
        print("opcion 1 administrador")
    case 2:
        print("opcion 2 usuario")
    case 3:
        print ("opcion 3 aprendiz")
    case _:
        print ("opcion no valida")

#ciclo for recorrido descendente 
for i in range (10, 0, -1):
    print (i)
print("______________________ejemplo intervalo de 2 en 2__________________")
for i in range(1,11,2):
    print(i)
    



