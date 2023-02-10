#Parametros son los que estan dentro de la funcion 
#Argumento Los que tu ingresas en la funcion


def saludos(name):
    print ("Que onda como estas, puto", name)

def potencia(base, exponente=2): #Puedes agregar un valor por default que puedes cambiar si lo deseas en caso de que no solo se queda el definido
    return base**exponente

name = input("Name: ")
saludos(name)

print (name) 

y = potencia(2, 3) #Posicion

y = potencia(exponente=3, base=2) #Puedes llamar directamente a la variable por su nombre 

y = potencia(2, exponente=3) #Nombre y posicion 

y = potencia(2) # Solo tienes un valor, pero ya tienes el =2 definido 


#Ejercicio 06 :D

def cuadratica (a,b,c):
    return  (-b+((b**2 - (4*a*c))**.5)) / 2 *a

x = cuadratica(1,c=15,b=-8)

print(x)
