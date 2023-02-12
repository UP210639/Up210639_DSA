'''  Comments

import mypkg.sibling (Llamar libreria) 
from mypkg import sibling (Llamar libreria)
import mypkg.slibing as sb (Abrebiar la libreria (Metodo)) 

'''
#Hash

# PEP 8  -- Style Guide for python code
# https://peps.python.org/pep-0008/

# Camello {FechaNacimiento o FecNac} Nomeclatura 
# Snake (Fecha_Nacimiento o Fec_Nac) Nomeclatura 

# Variables = Containers = Boxes 
# Python is a dinamically-typed language

_n = 1
n = 2
N = 3

Exchange_rate = None

m = 5 
m = "Hello"

keywords = ['False','None','True','True','Continue', 'and ', 'as', 'del', 'def' , 'assert' , 'break' , 'class','else','except', 'global'] #Palabras reservadas

keywords.insert(2, "Adios")

print (keywords[1], keywords.index('True')) #Busca la palabra en esa posicion # Busca la posicion de esa palabra 

print (keywords[-1]) #Numero negativos toma de abajo hacia arriba 

print (keywords.pop(), keywords.pop(), keywords.pop(1) , keywords[1], keywords.append('Hola'), keywords.pop()) #pop elimina y muestra el ultimo valor (Funciona como Lista y como pila)

print (keywords.count("True"))

print ("Conteo", len(keywords))

x = 2

x+=1 

print (x)

print (round (3.1416)) #Reduce el numero 

y = '3' + '2' #Concatena 

print (y)

a = 6
b = 3

a /= 2 * b  # ES IGUAL A a = a / (2 * b)

print (a)




#print ( "5" + 5 ) #Error en python 