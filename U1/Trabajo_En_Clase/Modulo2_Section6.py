import os 
import time 

print("What is your Last Name?")
Lastname = input()      #Input funciona para ingresar datos a las variables

print("What is your Name?")
Name = input()

print("Give a number")
Edad = int(input())     #Se le puede asignar el tipo de dato  por defecto siempre va a ser tipo char 

print(type(Edad))       #Te dice que tipo de variable es

Complete_Name = Name + " " + Lastname 

print("Hi", Complete_Name, "your number is ", Edad)

print ("Hola " * 2, 2 * "Adios ")


