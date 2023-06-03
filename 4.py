#suma de los elementos perisfericos
import random

m = int(input('Numero de filas de la Matriz: '))
n = int(input('Numero de columnas de la Matriz: '))

M = []
for i in range(m):
    M.append([])
    for j in range(n):
        M[i].append(random.randint(1, 9))

suma_periferica = 0
for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            suma_periferica += M[i][j]

for k in range(m):
    print()
    for j in range(n):
        print(M[k][j], end='\t')

print("\nLa suma de los elementos periféricos es:", suma_periferica)
