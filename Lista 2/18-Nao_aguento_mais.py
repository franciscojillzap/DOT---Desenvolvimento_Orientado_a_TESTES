'''
18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
'''

import random

def filtrar_negativos():
    X = []
    R = []
    
    for _ in range(10):
        X.append(random.randint(-20, 20))
        
    for i in range(10):
        if X[i] < 0:
            # Se for negativo, adiciona direto na lista R
            R.append(X[i])
            
    print(f"Lista X (com positivos e negativos): {X}")
    
    print(f"\nLista R (somente valores negativos): {R}")

filtrar_negativos()
