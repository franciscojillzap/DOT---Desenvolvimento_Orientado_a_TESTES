'''
Questão 9 – Contar palavras
Implemente contar_palavras(frase), separando palavras por um ou mais espaços em branco.
'''

def contar_palavras(frase):
	if type(frase) != str or len(frase) == 0:
		return Exception

	quant_palavras = frase.count(" ")

	return quant_palavras + 1

assert contar_palavras("") == Exception
assert contar_palavras(10) == Exception
assert contar_palavras("Eu estudo Python pela manhã") == 5
assert contar_palavras("Olá mundo") == 2
assert contar_palavras("Olá") == 1

print("todos os testes OK!")