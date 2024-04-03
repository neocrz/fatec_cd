"""
Name: icd004_04_02.py
Desc: Exercício - 
    implementar o código para multiplicação matricial das matrizes 3x3 A e B
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
def mul_matrix(m1, m2):
    if len(m1[0]) != len(m2): return False

    result = []
    n = len(m1)
    m = len(m2)
    o = len(m2[0])

    for i in range(n):
        result.insert(i, [])
        for j in range(m):
            result[i].insert(j, 0)
            for k in range(o):
                result[i][j] = result[i][j] + A[i][k] * B[k][j]

    return result

tempo_inicial = time()
e = 1000
for p in range(e):
    C = mul_matrix(A, B)
tempo_final = time()

print("\nSoma Matricial")
print("Matriz C:", C)
print(f"tempo de execução para {e} execuções: {tempo_final - tempo_inicial:.4f}")
