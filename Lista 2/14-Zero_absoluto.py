'''
Questão 14: Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
Escrever a lista C modificada.
'''

import random

def modificar_lista():
    C = []
    
    for _ in range(10):
        numero_sorteado = random.randint(-50, 50)
        C.append(numero_sorteado)
        
    print("Lista C original:")
    print(C)
    
    # Percorre a lista e troca os valores negativos por 0
    for i in range(10):
        if C[i] < 0:
            C[i] = 0
            
    print("\nLista C modificada (sem números negativos):")
    print(C)

modificar_lista()
