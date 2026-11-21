'''
Questão 15 – Ordenação por comprimento
Crie ordenar_por_tamanho(palavras), retornando nova lista ordenada pelo comprimento das strings,
mantendo a ordem original em caso de empate.

assert ordenar_por_tamanho(["sol", "a", "lua"]) == ["a", "sol", "lua"]
assert ordenar_por_tamanho([]) == []
'''

def ordenar_por_tamanho(palavras):
	if not isinstance(palavras, list):
		return Exception

	if not all(isinstance(x, str) for x in palavras):
		return Exception

	return sorted(palavras, key=len)

assert ordenar_por_tamanho("palavras") == Exception # Não é uma LISTA
assert ordenar_por_tamanho(["oi", "olá", 1]) == Exception # Tem um elemento fora do padrão STR

assert ordenar_por_tamanho(["sol", "a", "lua"]) == ["a", "sol", "lua"]
assert ordenar_por_tamanho([]) == []

print("Todos os teste OK!")