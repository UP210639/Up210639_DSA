print ("Hora de inicio (Hora, Minuto)")
Horas = int (input()) 
Minutos = int (input())

print ("Duracion del procceso (En minutos)")
Duracion = int(input())

y = Minutos + Duracion

x = y // 60 
Min = (y % 60) 

H = Horas + x
H = H % 24


print ("Tardo ", H ,":", Min)


