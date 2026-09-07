'''
10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.
'''

from random import randint

max_lista = 15

def gravar_lista():
	lista = []

	for i in range(max_lista):
		numero = randint(0, 100)
		lista.append(numero)

	return lista

def maior_e_posicao(lista):
	num_maior = max(lista)
	posicao_maior = lista.index(num_maior)

	return f"Dentro da lista, {num_maior} é o maior número e se encontra na {posicao_maior}ª posição."

def menor_e_posicao(lista):
	num_menor = min(lista)
	posicao_menor = lista.index(num_menor)

	return f"Dentro da lista, {num_menor} é o menor número e se encontra na {posicao_menor}ª posição."


lista_bacana = gravar_lista()
print(lista_bacana)

print(maior_e_posicao(lista_bacana))
print(menor_e_posicao(lista_bacana))