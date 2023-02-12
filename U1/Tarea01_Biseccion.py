#x^2 - 8x + 15

def fun(x):
    r = float
    r = (x**2) - (8*x) + 15
    return r

x1 = 4
x2 = 7
Xp = float

Er = 0.0001
Ee = abs(x2-x1)
i = 0

while Er > Ee:

    Xp = (x1 + x2)/2
    y1 = fun(x1)
    y2 = fun(Xp)
    if y1*y2 < 0:
        x2 = Xp
    else:
        x1 = Xp
    Er = abs(x2-x1)
    i= i + 1

print (f"i = {i}, raiz = {Xp}" )
print ("Hecho...")

