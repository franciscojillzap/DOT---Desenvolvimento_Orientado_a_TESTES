'''
17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.
'''

import random

def buscar_valor():
    W = []
    
    for _ in range(10):
        W.append(random.randint(1, 10))
        
    print(f"Lista W: {W}")
    
    V = int(input("\nDigite um valor V (de 1 a 10) para buscar na lista: "))
    
    # Inicializa o contador e uma lista para guardar as posições
    contagem = 0
    posicoes = []
    
    for i in range(10):
        if W[i] == V:
            contagem += 1
            posicoes.append(i)
            
    print(f"\nO valor {V} aparece {contagem} vez(es) na lista W.")
    
    if contagem > 0:
        print(f"Ele foi encontrado nas posições (índices): {posicoes}")
    else:
        print("Esse valor não está presente na lista.")

buscar_valor()
