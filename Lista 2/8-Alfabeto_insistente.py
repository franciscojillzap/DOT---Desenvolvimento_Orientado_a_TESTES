'''
8-Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra ‘A’.
'''

def contar(lista):
	qtd = lista.count("A")

	return f'A letra "A" foi repetida {qtd} vezes.'

alfabeto = []

for i in range(5):
	letra = input(f'Digite a {i+1}ª letra: ').upper()
	alfabeto.append(letra)

print(contar(alfabeto))