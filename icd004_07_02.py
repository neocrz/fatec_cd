"""
Name: icd004_07_02.py
Desc: Exemplo do slide - busca em lista linear retornando os campos das chaves
"""
from time import time

L = [1, "Goiânia", "Goiás", 2, "Bonito", "Mato Grosso", 3, "Carangola", "Minas Gerais", 4, "Peruíbe", "São Paulo", 20, "Serra", "Espírito Santo"]
n = len(L)
print("Dimensão da lista 'L':", n)
print("\n")

def busca_linear(x):
    for p in range(1):
        i = 0
        while i < n:
            if L[i] == x:
                return L[i], L[i+1], L[i+2]
            i = i + 1

tempo_inicial = time()
print("chave(1) =", busca_linear(1))
print("chave(2) =", busca_linear(2))
print("chave(3) =", busca_linear(3))
print("chave(4) =", busca_linear(4))
print("chave(20) =", busca_linear(20))
print("chave(0) =", busca_linear(0))
print("chave(6) =", busca_linear(6))
tempo_final = time()

print("Tempo de execução:", tempo_final - tempo_inicial)
