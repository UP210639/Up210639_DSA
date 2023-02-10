def ordenar(stack):
    return len(stack) == 0

def doble(x):
    y = x*2
    return y

a = [5,6,7,8,10]

for i in range(0, len(a)):
    print(a[i])

for i in range(0, len(a)+1 - 2):
    for j in range(0, len(a)+ 1 - i - 2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x

print(a)

b = 10

if b > 10:
    print ("Mayor a 10")
else:
    print ("Menor a 10")
    print ("Toy en el if")

print (doble(10))