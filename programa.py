import random

m = int(input('Numero de filas de la Matriz: '))
n = int(input('Numero de columnas de la Matriz: '))

M = []
for i in range(m):
  M.append([])
  for j in range(n):
    M[i].append(random.randint(1,9))

for k in range(m):
  print()
  for j in range(n):
    print(M[k][j], end = '\t')