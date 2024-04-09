"""
Name: icd004_07_01.py
Desc: Exemplo do slide - busca em lista linear
"""
from time import time

L = [1, "Goiânia", "Goiás", 2, "Bonito", "Mato Grosso", 3, "Carangola", "Minas Gerais", 4, "Peruíbe", "São Paulo", 20, "Serra", "Espírito Santo"]
n = len(L)
print("Dimensão da lista 'L':", n)
print("L[0]", L[0])
print("L[3]", L[3])
print("L[6]", L[6])
print("L[9]", L[9])
print("L[4]", L[4])
print("L[4][2]", L[4][2])
print("L[2][1]", L[2][1])
print("\n")

def busca_linear(x):
    for p in range(1):
        i = 0
        while i < n:
            if L[i] == x:
                return i
            i = i + 1

tempo_inicial = time()
print("índice da chave(5) =", busca_linear(5))
print("índice da chave(1) =", busca_linear(1))
print("índice da chave(4) =", busca_linear(4))
print("índice da chave(3) =", busca_linear(3))
print("índice da chave(2) =", busca_linear(2))
print("índice da chave(0) =", busca_linear(0))
print("índice da chave(20) =", busca_linear(20))
tempo_final = time()

print("Tempo de execução:", tempo_final - tempo_inicial)
