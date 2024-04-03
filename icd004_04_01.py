"""
Name: icd004_04_01.py
Desc: Exerício - 

Dadas as duas matrizes A e B implementar o algoritmo para soma matricial das matrizes 3x3
"""
# importando a função time de time
from time import time

# duas matrizes do enunciado
A = [[2, -1, 3],
     [0,4,-6],
     [-6,10,-5]]
B = [[4,7,-8],
     [9,3,5],
     [1,-1,2]]

# função que efetua a soma
def sum_matrix(m1, m2):
    if (len(m1) != len(m2)) or (len(m1[0]) != len(m2[0])): return False

    result = []
    n = len(m1)

    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(m1[i][j] + m2[i][j])

    return result

tempo_inicial = time()
e = 1000
for p in range(e):
    C = sum_matrix(A, B)
tempo_final = time()

print("\nSoma Matricial")
print("Matriz C:", C)
print(f"tempo de execução para {e} execuções: {tempo_final - tempo_inicial:.4f}")
