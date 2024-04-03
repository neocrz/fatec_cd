"""
Name: icd004_03_01.py
Desc: Multiplicação de matrizes. Exemplo do slide.
"""

from time import time

A = [[5,8],[1,0],[2,7]]
B = [[-4,-3],[2,0]]

C = [[0,0],[0,0],[0,0]]
print("Matriz A:")
print("A[0][0]:",A[0][0])
print("A[0][1]:",A[0][1])
print("A[1][0]:",A[1][0])
print("A[1][1]:",A[1][1])
print("A[2][0]:",A[2][0])
print("A[2][1]:",A[2][1])

print("Matriz B:")
print("B[0][0]:",B[0][0])
print("B[0][1]:",B[0][1])
print("B[1][0]:",B[1][0])
print("B[1][1]:",B[1][1])

tempo_inicial = time()
for p in range(1000):
    for i in range(0,3):
        for j in range(0,2):
            C[i][j] = 0
            for k in range(0, 2):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

tempo_final = time()
print("\nProduto Matricial")
print("Matriz C:", C)
print("tempo de execução", tempo_final - tempo_inicial)
