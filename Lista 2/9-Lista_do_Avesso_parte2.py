'''
9-Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.
'''
from random import randint

max_lista = 5

def ordem_inversa(lista):
    return lista[::-1]

X = []

for i in range(max_lista):
    numero = randint(0, 100)
    X.append(numero)

Y = ordem_inversa(X)

print(f"Esta é a lista original criada: {X}")
print(f"Esta é a lista inversa: {Y}")