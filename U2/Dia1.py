#Proceso Posfix a valor   (ab+) Pos
#Proceso InFix a PosFix   (+ab) Pre
#Proceso Infix            (a+b) In

# "5 * ( 6 + 2 ) - 12 / 4" = Infix
# "5 6 2 + * 12 4 / -"     = PosFix  Llega al operador y retrocede 2 lugar atras y aplica el operador en esos 2 numeros 

'''
Algoritmo de posfix a valor
P = posfix
Value = Resultado

Add ")" at the final P as centinela 
Scan F untill find ")"
    a) B = pop from stack, A=pop from stack
    b) C = A operator B
    C) push (C) to stack
value = pop from stack
'''
i=0
e=0
p = [5, 6, 2,'+','*',12,4,'/','-']
B = []

p.append(')')

while p[i] != ')':
    if type(p[i]) == int:
        B.append(p[i]) 
        i=i+1
    elif type(p[i]) == str:
        if p[i] == '+':
            b = B.pop()
            a = B.pop()
            c = a + b
            B.append(c)
            i=i+1
        elif p[i] == '-':
            b = B.pop()
            a = B.pop()
            c = a - b
            B.append(c)
            i=i+1
        elif p[i] == '*':
            b = B.pop()
            a = B.pop()
            c = a * b
            B.append(c)
            i=i+1
        else:
            b = B.pop()
            a = B.pop()
            c = a / b
            B.append(c)
            i=i+1
print (B)


