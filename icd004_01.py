"""
Name: icd004_01.py
Desc:
    Exemplo - inversão de uma sequência numéria, ultimo troca com o primeiro, antepenultimo com o segundo etc.
"""

from time import time

n = 11
S = [x for x in range(n)]

print("vetor S =  ", S)
tempo_inicial = time()
for i in range(0, int((n/2))):
    temporario = S[i]
    S[i] = S[(n-1) - i]
    S[(n-1) - i] = temporario
tempo_final = time()

print("Vetor S invertido = ", S)
print("Tempo de execução = ", tempo_final - tempo_inicial)
