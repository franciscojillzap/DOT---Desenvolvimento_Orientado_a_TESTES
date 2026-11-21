'''
Questão 12 – Interseção de listas
Crie intersecao(a, b), retornando os elementos presentes em ambas as listas, sem repetições e na
ordem de primeira aparição em a. Considere elementos inteiros.

assert intersecao([3, 1, 2, 1], [1, 3]) == [3, 1]
assert intersecao([1, 2], [3]) == []
'''

def intersecao(a, b):
	# Verifica se A e B são listas
	if not isinstance(a, list) or not isinstance(b, list):
		return Exception

	# Verifica se os valores dentro de A e B são inteiros
	if not all(isinstance(x, int) for x in a + b):
		return Exception

	resultado = []

	for numero in a:
		# Verifica se o elemento de A está em B
		# Impede que um valor que já foi adicionado ao resultado se repita
		if numero in b and numero not in resultado:
			resultado.append(numero)

	return resultado

assert intersecao(1, 2) == Exception # Não é lista
assert intersecao([1, 2, "tres"], [1, 2, 3.5]) == Exception # Tipo STR e FLOAT na lista

assert intersecao([3, 1, 2, 1], [1, 3]) == [3, 1]
assert intersecao([1, 2], [3]) == []

print("Todos os testes OK!")