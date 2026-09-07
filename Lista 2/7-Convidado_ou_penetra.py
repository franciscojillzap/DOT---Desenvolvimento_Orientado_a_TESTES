'''
7-Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
outro valor dado pertence ou não à lista.
'''

from random import randint

max_lista = 10

def gravar_lista():
	lista = []

	for i in range(max_lista):
		numero = randint(1, 50)
		lista.append(numero)

	return lista

def encontrar_valor(lista, numero):
	if numero in lista:
		return f"{numero} foi encontrado na lista!"
	else:
		return f"{numero} não se encontra na lista..."

lista_bacana = gravar_lista()
print(lista_bacana)

chute = int(input("Digite um valor que deseja saber se encontra-se na lista: "))

print(encontrar_valor(lista_bacana, chute))
