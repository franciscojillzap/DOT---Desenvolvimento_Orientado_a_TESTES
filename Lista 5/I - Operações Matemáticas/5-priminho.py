'''
Questão 5 – Número primo
Implemente eh_primo(numero). Teste primos, compostos, zero, um e negativos.
'''

def eh_primo(numero):
	# Número Primo dever ser Inteiro
	if type(numero) != int:
		return Exception

	# Número Primo deve ser maior que 1
	if numero < 2:
		return False

	# Número Primo só é divisível por 1 e por ele mesmo
	for i in range(2, numero):
		if numero % i == 0:
			return False

	return True

# Valores Válidos
assert eh_primo(0) == False
assert eh_primo(1) == False
assert eh_primo(7) == True # Primo
assert eh_primo(9) == False # Composto

# Valores Improváveis e Inválidos
assert eh_primo(-1) == False
assert eh_primo("um") == Exception

print("Todos os testes OK!")