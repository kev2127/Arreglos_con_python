#Formas de controlar while
""""
identificadores o tipos de primitivos
por numeros sea reales o enteros 
por boleanos 
por cadenas de texto

no primitivos 
listas 
tuplas 
diccionario
sets
ranges 
arreglos  : vectore, matrices
"""

#region control letra
palabra = input("ingrese una palabra: ")
while palabra.lower()== "s":
    palabra =input ("ingrese una palabra: ")
print("Fin del ciclo" \
"")
#endregion

#region control de FALSE O TRUE
contador = 0
while True:
    if contador ==10:
        print (contador)
        break
        
    else:
        print("El contador no ha llegado a 10")
        contador += 1

print("El ciclo while ha terminado correctamente")
contador += 1
#endregion