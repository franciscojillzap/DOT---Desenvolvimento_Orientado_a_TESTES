'''
Questão 15: Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.
'''

import random

def inverter_lista():
    D = []
    E = []
    
    for _ in range(10):
        D.append(random.randint(1, 100))
        
    # range(INÍCIO, FIM, PASSO)
    # INÍCIO - O fim é o começo, inicia no ÚLTIMO índice (9)
    # FIM - O começo é o fim, termina no PRIMEIRO índice (0)
    # PASSO - faz o moonwalk, ordem DECRESCENTE
    for i in range(9, -1, -1):
        E.append(D[i])
        
    print("Lista D (Original):")
    print(D)
    
    print("\nLista E (Invertida):")
    print(E)

inverter_lista()
