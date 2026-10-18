'''
20. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o somatório desse valor.
'''

def somatorio(n):
	if type(n) != int or n <= 0:
		return Exception

	numeros = []

	for i in range(1, n+1):
		numeros.append(i)

	soma_total = sum(numeros)

	return soma_total

# Testes com valores INVÁLIDOS
assert somatorio(0) == Exception
assert somatorio(-1) == Exception
assert somatorio("1") == Exception

# Testes com valores VÁLIDOS
assert somatorio(5) == 15
assert somatorio(8) == 36
assert somatorio(10) == 55 

print("Questão 20 ok!")
