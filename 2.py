#suma de los elementos de la triangular inferior
import random

m = int(input('Numero de filas de la Matriz: '))
n = int(input('Numero de columnas de la Matriz: '))

M = []
for i in range(m):
  M.append([])
  for j in range(n):
    M[i].append(random.randint(1,9))

sum_triangular = 0
for i in range(m):
  for j in range(n):
    if j <= i:  # Verifica si el elemento está en la triangular inferior
      sum_triangular += M[i][j]

for k in range(m):
  print()
  for j in range(n):
    print(M[k][j], end = '\t')

print("\nLa suma de los elementos de la triangular inferior es:", sum_triangular)
