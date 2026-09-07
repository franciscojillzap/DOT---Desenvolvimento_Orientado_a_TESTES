'''
Questão 13: Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face.
'''

import random

def simular_dados():
    n = int(input("Digite o número de lançamentos de um dado: "))
    
    contadores = [0] * 7
    
    for i in range(n):
        resultado = random.randint(1, 6)
        contadores[resultado] += 1
        
    print(f"\nO Resultado de {n} lançamentos foi...")
    for face in range(1, 7):
        print(f"Face {face}: caiu {contadores[face]} vez(es)")

# Executa a simulação
simular_dados()
