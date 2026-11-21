'''
Questão 14 – Filtrar valores acima do limite
Crie filtrar_maiores(numeros, limite), retornando, na ordem original, somente os números
estritamente maiores que o limite.

assert filtrar_maiores([2, 7, 5, 9], 5) == [7, 9]
assert filtrar_maiores([1, 2], 5) == []
'''

def filtrar_maiores(numeros, limite):
	if not isinstance(numeros, list) or not isinstance(limite, int):
		return Exception

	if not all(isinstance(x, (int, float)) for x in numeros):
		return Exception

	resultado = []

	for num in numeros:
		if num > limite and num not in resultado:
			resultado.append(num)

	return resultado

assert filtrar_maiores(1, 1) == Exception # numeros não é LISTA
assert filtrar_maiores([1, 2, 3], "quatro") == Exception # limite não é inteiro

assert filtrar_maiores([2, 7, 5, 9], 5) == [7, 9]
assert filtrar_maiores([1, 2], 5) == []
assert filtrar_maiores([4, 5, 5, 6], 4) == [5, 6] # Valores repetidos

print("Todos os testes OK!")