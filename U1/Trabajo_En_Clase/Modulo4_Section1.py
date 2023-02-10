# pip install numpy

#import numpy as np

def ispar(x): #Funcion definida
    if x %2 == 0:
        return True
    else:
        return False

print(ispar(50))

y=(lambda x:x+3)(4) #Lamda funcion flexible (Funcion | valor)
print(y)

lista = [4,7,1]
 
ordenada = sorted(lista) #Funcion pre costruida  :D

y=list(map(lambda x:x+3, lista)) #Aplica la funcion a toda la matriz, lista o vector :D

print (y)

mayores = list(filter(lambda x: x>4, lista))

print (mayores)

a = 10
b = 0

c = a/b if b!=0 else -1 # Operador ternario | if condicion | Si | No |

print (c)


