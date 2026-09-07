'''
19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X.
'''

import random

def juntar_listas():
    R = []
    S = []
    X = []
    
    # Preenche a lista R com 5 números aleatórios
    for _ in range(5):
        R.append(random.randint(1, 50))
        
    # Preenche a lista S com 10 números aleatórios
    for _ in range(10):
        S.append(random.randint(1, 50))
        
    # Copia os 5 elementos de R para X
    for i in range(5):
        X.append(R[i])
        
    # Copia os 10 elementos de S para X
    for i in range(10):
        X.append(S[i])
        
    # Passo 5: Exibe todas as listas
    print("Lista R (5 elementos):", R)
    print("Lista S (10 elementos):", S)
    print("\nLista X (15 elementos):", X)

juntar_listas()
