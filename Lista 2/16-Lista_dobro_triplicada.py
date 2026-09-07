'''
16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: 
	--Elementos de Y com índice par receberão os respectivos elementos de X divididos por 2;
	--Elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Escrever as listas X e Y.
'''

import random

def processar_listas():
    X = []
    Y = []
    
    for _ in range(10):
        X.append(random.randint(1, 50))
        
    for i in range(10):
        # Verifica se o ÍNDICE atual (i) é par
        if i % 2 == 0:
            # Índice par: elemento de X dividido por 2
            resultado = X[i] // 2
        else:
            # Índice ímpar: elemento de X multiplicado por 3
            resultado = X[i] * 3
            
        Y.append(resultado)
        
    print(f"Lista X (Original): {X}")
    print(f"\nLista Y (Processada): {Y}")
    
processar_listas()
