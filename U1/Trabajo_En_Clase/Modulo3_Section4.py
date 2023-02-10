a = 5

b = a

print (a)

a = 6

print (b)

list_1 = [3,5]

list_2 = list_1  # No pasa los valores pasa la memoria de la lista y ambas listas comparte siempre la memoria si cambias 2 cambias 1 y biseversa :D

print (list_2)

list_1[0] = 10 

print (list_2)


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = list1[:] # : = pasa los datos no la direccion 

list1[0] = 10 

print(list2)

print(list1)
print(list1[2:4])
print(list1[:])
print(list1[0 : len(list1)])
print(list1[1:-1])
print(list1[1:])
print(list1[:4])


del list1[1:3]
del list1[:]
del list1

my_list = [10, 2, 12, 8, 2]

print(12 in my_list)

largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i

    
print(largest)