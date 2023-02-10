counter = -3
while counter:  #(Si no se agrega ninguna condicion python lo toma como valor boleando hasta que sea 0 se terminara el ciclo )
    print ("inside the loop", counter)
    counter += 1 
print ("End of the loop")

# for i in range(10):  (0, (valorn inicial), 0 (valor final),0 (aumento)) 

#Continue , pass y break

edad = 18
'''
if edad < 18:
    pass    #No hace nada
else:
    Nombre=int(input())
    edad=int(input())
'''

for i in range(10):
    #continue
    print(i)
    #break
print("Fin")

user_word = input("Dime una palabra")
user_word = user_word.upper()
new_word = " "
for letter in user_word:
    if letter not in ("A","E","I","O","U"):
        new_word += letter
print(new_word)

for i in range(3):
    print(i)
else:                  #Otra manera de hacer una condicion despues (No es recomendable)
    print("else", i)

# Para acomodar listas :D 

my_list = [10,9,2,3,4]

swapped = True 

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

my_list.reverse()

print(my_list)

     
