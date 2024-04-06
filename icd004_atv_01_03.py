import random
from time import time

# função de ordenação por inserção: recebe uma lista e o número de vezes que vai executar (padrão 30000)
def ordenação_inserção(lista, vezes=30000):
    for p in range(vezes):
        for j in range(1, len(lista)):
            temp = lista[j]
            i = j - 1
            while i >= 0 and lista[i] > temp:
                lista[i + 1] = lista[i]
                i = i-1
            lista[i + 1] = temp

crescente = [x for x in range(0, 50)]
print("Lista 'crescente':",crescente)
print("Dimensão de 'crescente':", len(crescente))
crescente_inicial = time()
ordenação_inserção(crescente)
crescente_final = time()
print("Lista 'crescente' ordenada:", crescente)
print("tempo de execução de 'crescente':", crescente_final - crescente_inicial)

decrescente = [x for x in range(0, 50)][::-1]
print("Lista 'decrescente':",decrescente)
print("Dimensão de 'decrescente':", len(decrescente))
decrescente_inicial = time()
ordenação_inserção(decrescente)
decrescente_final = time()
print("Lista 'decrescente' ordenada:", decrescente)
print("tempo de execução de 'decrescente':", decrescente_final - decrescente_inicial)

aleatória = random.sample(range(0, 50), 50)
print("Lista 'aleatória':",aleatória)
print("Dimensão de 'aleatória':", len(aleatória))
aleatória_inicial = time()
ordenação_inserção(aleatória)
aleatória_final = time()
print("Lista 'aleatória' ordenada:", aleatória)
print("tempo de execução de 'aleatória':", aleatória_final - aleatória_inicial)

crescente100 = [x for x in range(0, 100)]
print("Lista 'crescente100':",crescente100)
print("Dimensão de 'crescente100':", len(crescente100))
crescente100_inicial = time()
ordenação_inserção(crescente100)
crescente100_final = time()
print("Lista 'crescente100' ordenada:", crescente100)
print("tempo de execução de 'crescente100':", crescente100_final - crescente100_inicial)

decrescente100 = [x for x in range(0, 100)][::-1]
print("Lista 'decrescente100':",decrescente100)
print("Dimensão de 'decrescente100':", len(decrescente100))
decrescente100_inicial = time()
ordenação_inserção(decrescente100)
decrescente100_final = time()
print("Lista 'decrescente100' ordenada:", decrescente100)
print("tempo de execução de 'decrescente100':", decrescente100_final - decrescente100_inicial)

aleatória100 = random.sample(range(0, 100), 100)
print("Lista 'aleatória100':",aleatória100)
print("Dimensão de 'aleatória100':", len(aleatória100))
aleatória100_inicial = time()
ordenação_inserção(aleatória100)
aleatória100_final = time()
print("Lista 'aleatória100' ordenada:", aleatória100)
print("tempo de execução de 'aleatória100':", aleatória100_final - aleatória100_inicial)