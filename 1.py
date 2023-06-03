#suma de los elementos de la diagonal secundaria

import random

m = int(input('Numero de filas de la Matriz: '))
n = int(input('Numero de columnas de la Matriz: '))

M = []
for i in range(m):
    M.append([])
    for j in range(n):
        M[i].append(random.randint(1, 9))

# Imprimir matriz original
print("Matriz Original:")
for k in range(m):
    print()
    for j in range(n):
        print(M[k][j], end='\t')

# Calcular suma de la diagonal secundaria
suma = 0
for i in range(m):
    suma += M[i][n - i - 1]

print("\n\nLa suma de la diagonal secundaria es:", suma)
