import time
import os

inicio = time.time()
print("For")
for i in range (5):
    print(i)

fin = time.time()
tiempoFinal = fin - inicio 

print (f"""tiempo de ejecucion: {tiempoFinal}""")
contador = 0
time.sleep(5)
os.system('cls')



print("While")

while contador <= 10:
    print(contador)
    contador += 1
fin = time.time()

print (f""" Tiempo de ejecucion: {tiempoFinal}""")
contador = 0