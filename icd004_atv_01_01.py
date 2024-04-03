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
    if (len(m1) != len(m2)) or (len(m1[0]) != len(m2[0])): return False, False
    op = 0

    result = []
    n = len(m1)

    for i in range(n):
        op +=1
        result.append([])
        for j in range(n):
            op +=1
            result[i].append(m1[i][j] + m2[i][j])

    return result, op

# função que efetua a multiplicação
def mul_matrix(m1, m2):
    if len(m1[0]) != len(m2): return False, False
    op = 0
    result = []
    n = len(m1)
    m = len(m2)
    o = len(m2[0])

    for i in range(n):
        op +=1
        result.insert(i, [])
        for j in range(m):
            op +=1
            result[i].insert(j, 0)
            for k in range(o):
                op +=1
                result[i][j] = result[i][j] + A[i][k] * B[k][j]

    return result, op # retornar a matriz e o numero de operações

e = 1000

sum_tinicial = time()
for p in range(e):
    C, sum_op = sum_matrix(A, B)
sum_tfinal = time()
print("Matriz A:",A)
print("Matriz B:",B)

print("\n==== Soma Matricial ====")
print("Matriz C:", C)
sum_tempo = sum_tfinal - sum_tinicial
print(f"tempo de execução para {e} execuções: {sum_tempo:.4f}. nº Operação dominante: {sum_op}")

mul_tinicial = time()
for p in range(e):
    C, mul_op = mul_matrix(A, B)
mul_tfinal = time()
mul_tempo = mul_tfinal - mul_tinicial
print("\n==== Multiplicação Matricial ====")
print("Matriz C:", C)
print(f"tempo de execução para {e} execuções: {mul_tempo:.4f}. nº Operação dominante: {mul_op}")
print(f"\nRelação (Multiplicação/Soma): {mul_tempo / sum_tempo}" )

print('''
Logo, podemos notar que a operação de multiplicação tem maior número de operações dominantes realizadas
e tem maior tempo de execução.
''')