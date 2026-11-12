'''
Questão 2 – Maior de três números
Implemente maior(a, b, c), retornando o maior valor. Inclua valores iguais, negativos e zero.
'''

def maior(a, b, c):
	if any(not isinstance(x, int) for x in [a, b, c]):
		return Exception

	# Maneira 1
	maior = a

	if b > maior:
		maior = b
	elif c > maior:
		maior = c

	# Maneira 2
	maior_valor = max(a, b, c)

	return maior_valor

# Valores Válidos (Iguais, Negativos e Zero)
assert maior(5, 5, 5) == 5
assert maior(-15, -10, -5) == -5
assert maior(15, 0, -15) == 15

# Valor Improvável
assert maior("cinco", 10, "quinze") == Exception

print("Todos os testes OK!")