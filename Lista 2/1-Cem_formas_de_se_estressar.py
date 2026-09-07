'''
1-Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
	a) Mostre a quantidade de números pares;
	b) Grave uma lista somente com os números pares e mostre a lista;
	c) Mostre a quantidade de números ímpares;
	d) Grave uma lista somente com os números ímpares e mostre a lista.
'''

from random import randint

# 1 - Lista com 100 números
def gravar_lista():
	lista = []

	for i in range(100):
		lista.append(randint(0, 100))

	return lista

# A & B - Números PARES
def so_par(lista):
	lista_par = []

	for num in lista:
		if num % 2 == 0:
			lista_par.append(num)

	print(f"Há {len(lista_par)} números pares nesta lista. Dentre eles temos:")
	print(lista_par)

# C & D - Números ÍMPARES
def so_impar(lista):
	lista_impar = []

	for num in lista:
		if num % 2 != 0:
			lista_impar.append(num)

	print(f"Há {len(lista_impar)} números ímpares nesta lista. Dentre eles temos:")
	print(lista_impar)


lista_original = gravar_lista()
so_par(lista_original)
so_impar(lista_original)
