"""
Name: icd004_05_01.py
Desc:
    Exemplo do slide. Algoritmo de ordenação por inserção.
"""

from time import time

A = [5, 2, 4, 6, 1, 3]

print("Matriz A:",A)
print("Dimensão de A:", len(A))

tempo_inicial = time()
for p in range(1):
    for j in range(1, len(A)):
        temp = A[j]
        i = j - 1
        while i >= 0 and A[i] > temp:
            A[i + 1] = A[i]
            i = i-1
        A[i + 1] = temp
tempo_final = time()

print("A ordenada:", A)
print("tempo de execução:", tempo_final - tempo_inicial)