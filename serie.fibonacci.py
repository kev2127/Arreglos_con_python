#region serie fibonacci

#es sin usa DEF es decir sin funciones 
# fn = f-1 + f-2
#f-1 va ser "a"
#f-2 va ser "b"
#Fn resultado final
a,b = 0,1
#a=0 b=1

#iterante es una variable que tendra un comportamiento 
#incrementar en el ciclo 

for i in range (10):
    print(a)
    a,b=b,a+a
    
    #a=b y b=a+b
#1 a,b=b, a+b a=1 b=0+0=0
#2 a,b=b,a+b a=0 b=1+0=1
#3 a,b=b,a+b a=1 b=0+1=1
#4 a,b=b,a+b a=1 b=1+1=2
#5 a,b=b,a+b a=1 b=1+2=3
#6 a,b=b,a+b a=2 b=2+3=5
#7 a,b=b,a+b a=3 b=3+5=8
#8 a,b=b,a+b a=5 b=5+8=13
#9 a,b=b,a+b a=8 b=8+13=21
#10 a,b=b,a+b a=13 b=13+21=34
#11 a,b=b,a+b a=21 b=21+34=55
#12 a,b=b,a+b a=34 b=34+55=89
#13 a,b=b,a+b a=55 b=55+89=144

nums = int(input("ingrese la cantidad de numeros a mostrar: "))
a,b = 0,1
for interante in range(nums):
    print(a)
    a,b = b,a+b



