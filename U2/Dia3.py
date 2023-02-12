'''
Algoritmo de infix a posfix
Q = infix expresion vector
P = posfis expresion vector

1.- put "(" at the begginning of expression Q and
    put ")" at the end of the expression Q
2.- Scan Q from left to right and repeat step 3 to 6 for each element of Q
    3.- if in operand in encountered add it to P
    4.- if is "(" push int onto stack
    5.- if an operator is encoutered then:
        a.  Repeatedly pop from the stack and add to P each operator (on top of stack)
            which has same or higher precedence than the operator
        b.  Add operator to stack 
    6.- if ")" is encountered then
        a.  Repetedly pop from the stack and add to p each operator (on top of stack) 
            until a "(" is encountered
        b.  pop from stack the left parenthesis. Do not add to p
'''
i=0
Q = '5 * (6 + 2) - 12 / 4' 
P = []

Q = Q.split()

Q.append(')')
Q.append('.')
Q.insert(0,'(')

while Q[i] != '.':
    if type(Q[i]) == int: 
        print("Numero") 
        i=i+1





