"""
Name: icd004_02_02.py
Desc: 
Exercício do slide - comparar o tempo de execução de soma de dois pares de matrizes.
A dimensão da segunda matriz deve ser o dobro da primeira. A matrizes são matrizes quadradas.
"""

import random
from time import time

# Função que gera matriz
def gen_matrix(n, empty=False):
    if empty:
        return [ [ 0 for i in range(n) ] for j in range(n) ]

    r_nums = random.sample(range(-100, 100), n*2*n*2)
    m = []
    k = 0
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(r_nums[k])
            k += 1
        m.append(temp)
        temp = []
    return m

# Função que soma matrizes
def sum_matrix(m1, m2, result):
    if (len(m1) != len(m2)) or (len(m1[0]) != len(m2[0])): return False

    n = len(m1)

    for i in range(n):
        for j in range(n):
            result[i][j] = m1[i][j] + m2[i][j]

    return result
            


n = 3

A1 = gen_matrix(n)
B1 = gen_matrix(n)
C1 = gen_matrix(n, empty = True)

n = n*2

A2 = gen_matrix(n)
B2 = gen_matrix(n)
C2 = gen_matrix(n, empty = True)

# número de vezes para somar
loop = 1000

print("A1:",A1)
print("B1:",B1)
print("C1:",C1)



c1_tinicial = time()
for p in range(loop):
    sum_matrix(A1, B1, C1)
c1_tfinal = time()

print("\nC1 após a soma:",C1)
print(f"tempo de execução de C1 com {loop} somas: {c1_tfinal - c1_tinicial:.4f}")
print("")
print("A2:",A2)
print("B2:",B2)
print("C2:",C2)



c2_tinicial = time()
for p in range(loop):
    sum_matrix(A2, B2, C2)
c2_tfinal = time()

print("\nC2 após a soma:",C2)
print(f"tempo de execução de C2 com {loop} somas: {c2_tfinal - c2_tinicial:.4f}")


