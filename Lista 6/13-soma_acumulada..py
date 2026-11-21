'''
Questão 13 – Lista acumulada
Crie soma_acumulada(numeros), retornando uma lista em que cada posição contém a soma dos
elementos até aquela posição.

assert soma_acumulada([2, 3, 5]) == [2, 5, 10]
assert soma_acumulada([]) == []
'''

def soma_acumulada(numeros):
	if not isinstance(numeros, list):
		return Exception

	if not all(isinstance(x, (int, float)) for x in numeros):
		return Exception

	soma_atual = 0
	resultado = []

	for num in numeros:
		soma_atual += num
		resultado.append(soma_atual)

	return resultado

assert soma_acumulada(1) == Exception
assert soma_acumulada([1, 2, "tres"]) == Exception

assert soma_acumulada([2, 3, 5]) == [2, 5, 10]
assert soma_acumulada([]) == []

print("Todos os testes OK!")