'''
6-Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a QUANTIDADE x PREÇO. 

Calcule e exiba também:
	-- Faturamento TOTAL que é o somatório de todos os faturamentos, 
	-- A MÉDIA dos faturamentos
	-- Quantos faturamentos estão ABAIXO da MÉDIA.
'''

from random import randint

max_lista = 20

def gravar_quantidade():
	lista_qtd = []

	for i in range(max_lista):
		quantidade = randint(1, 10)
		lista_qtd.append(quantidade)

	return lista_qtd

def gravar_preco():
	lista_prc = []

	for i in range(max_lista):
		preco = randint(1, 100)
		lista_prc.append(preco)

	return lista_prc

def gravar_faturamento(Q, P):
	lista_fatura = []

	for i in range(max_lista):
		fatura = Q[i] * P[i]
		lista_fatura.append(fatura)

	return lista_fatura

def calculos_faturamento(F):
	fatura_total = sum(F)
	media_fatura = round(sum(F) / len(F), 2)
	abaixo_media = []

	for fatura in F:
		if fatura < media_fatura:
			abaixo_media.append(fatura)

	return f'Faturamento TOTAL: R${fatura_total}\nMÉDIA dos Faturamentos: R${media_fatura}\nFaturas ABAIXO da MÉDIA: {abaixo_media}'

qtd_produtos = gravar_quantidade()
preco_produtos = gravar_preco()
fatura_compra = gravar_faturamento(qtd_produtos, preco_produtos)

print(f'Quantidades: {qtd_produtos}')
print(f'Preços: {preco_produtos}')
print(f'Faturamentos: {fatura_compra}\n')
print(calculos_faturamento(fatura_compra))

