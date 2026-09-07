'''
Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
elementos deste em uma outra lista de 20 elementos.
'''

from random import randint

max_lista = 10

def gravar_lista():
	lista = []

	for i in range(max_lista):
		numero = randint(0, 100)
		lista.append(numero)

	return lista

def intercalar_listas(l1, l2):
	resultado = []

	for i in range(max_lista):
		resultado.append(l1[i])
		resultado.append(l2[i])

	return resultado

lista1 = gravar_lista()
lista2 = gravar_lista()
lista_intercalada = intercalar_listas(lista1, lista2)

print(f"1ª Lista: {lista1}")
print(f"2ª Lista: {lista2}")
print(f"1ª e 2ª Lista intercaladas: {lista_intercalada}")