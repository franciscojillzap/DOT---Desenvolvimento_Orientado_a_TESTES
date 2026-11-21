'''
Questão 11 – Rotação de lista
Crie rotacionar_direita(lista, k), retornando nova lista deslocada K posições para a direita; 
	# K deve ser inteiro não negativo.

assert rotacionar_direita([1, 2, 3, 4], 1) == [4, 1, 2, 3]
assert rotacionar_direita([], 3) == []
'''

def rotacionar_direita(lista, k):
    # Valida se 'k' é um inteiro válido e não negativo.
    if not isinstance(k, int) or k < 0:
        return Exception
    
    # Se a lista estiver vazia, retorna uma nova lista vazia imediatamente
    if not lista:
        return []
    
    # Calcula o deslocamento real usando o resto da divisão (%).
    	# Ex: Em uma lista de 4 itens, deslocar 5 vezes equivale a deslocar apenas 1.
    k = k % len(lista)
    
    # Realiza o deslocamento usando fatiamento:
    	# Se k > 0: pega os últimos 'k' itens (lista[-k:]) e junta com o restante (lista[:-k]).
    	# Se k == 0: usa lista[:] para retornar uma cópia nova sem alterar a ordem.
    return lista[-k:] + lista[:-k] if k else lista[:]

assert rotacionar_direita([1, 2, 3, 4], 1) == [4, 1, 2, 3]
assert rotacionar_direita([], 3) == []

print("testes ok")