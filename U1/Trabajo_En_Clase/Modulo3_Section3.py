import numpy as np 

squares = [x ** 2 for x in range(10) if x**2 % 2 ==0]  #(operacion || cantidad de numeros || si se desea meter un filtro)

print(squares) 


board = []

# lists in list

for i in range(8):
    row = ["A" for i in range (8)]
    board.append(row)

print(board)



# Tipos de matrices dimensional bidimensional y tridimensional  (Se puede incluso una matriz de n dimesiones )


a = np.array([7,2,4])

b = np.array([[1, 2, 3, 5],
              [4, 5, 6, 15],
              [7, 9, 8, 24],]) #Matriz de 3 x 4

c = np.array([[[2,17,23,1],[2,17,23,1],[2,17,23,1]],
              [[2,17,23,1],[2,17,23,1],[2,17,23,1]]])

print("c", c.shape) #Da las dimensiones de la matrices 
print(c[1],[2],[3]) # Llama un dato de las cordenadas 

print(b.shape) 
print(b.shape[0]) # longitud de la matriz 
print(b[2,1])

print(np.where(a > 3)) #Busca los valores que tengan sentido con la condicion (solo te trae la posicion :D)



board1 = [[i + j for j in range (3)] for i in range (7)]

board2 = np.array(board1)

print("F, C", board2.shape)

print("Len ", len(board1))

print(board1) , print()

#para tomar datos de una parte especifica y desglosar por dato 

for day in board1:
    for item in day:
        print(item, end = "\t")
    print()
print()


# 3 EDIFICIOS CADA EDIFICIO DE 15 PISOS EN CADA PISO 20 CUARTOS 

Roomes = [ [ [False for r in range (20)] for f in range (15) ]  for b in range(3) ]

