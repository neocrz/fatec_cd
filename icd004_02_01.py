"""
Name: icd004_02_01.py
Desc: Exemplo do slide - algoritmo de soma de matrizes de dimensões iguais
"""


from time import time

A = [[2, -1, 3],
     [0, 4, 6],
     [-6, 10, -5]]

B = [[4, 7, -8],
     [9, 3, 5],
     [1, -1, 2]]

C = [[0,0,0],[0,0,0],[0,0,0]]


print("Matriz A")
print("A[0][0] = ", A[0][0])
print("A[0][1] = ", A[0][1])
print("A[0][2] = ", A[0][2])
print("A[1][0] = ", A[1][0])
print("A[1][1] = ", A[1][1])
print("A[1][2] = ", A[1][2])
print("A[2][0] = ", A[2][0])
print("A[2][1] = ", A[2][1])
print("A[2][2] = ", A[2][2])

print("Matriz B")
print("B[0][0] = ", B[0][0])
print("B[0][1] = ", B[0][1])
print("B[0][2] = ", B[0][2])
print("B[1][0] = ", B[1][0])
print("B[1][1] = ", B[1][1])
print("B[1][2] = ", B[1][2])
print("B[2][0] = ", B[2][0])
print("B[2][1] = ", B[2][1])
print("B[2][2] = ", B[2][2])

tempo_inicial = time()
for p in range(1):
    for i in range(0,3):
        for j in range(0, 3):
            C[i][j] = A[i][j] + B[i][j]
tempo_final = time()

print("Soma matricial:")
print("MATRIZ C = ", C)
print("Tempo de execução = ", tempo_final - tempo_inicial)

