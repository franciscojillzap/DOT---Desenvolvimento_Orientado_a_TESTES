'''
12-Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os ordenados em ordem crescente.
'''

def ordem_e_progresso(n1, n2):
	if type(n1) != int or type(n2) != int:
		return Exception

	if n1 >= n2:
		return n2, n1
	else:
		return n1, n2

# Testes de Valores INVÁLIDOS
assert ordem_e_progresso(12.8, 4) == Exception # Número 1 é FLOAT
assert ordem_e_progresso(10, "5") == Exception # Número 2 é STRING

# Testes com Valores VÁLIDOS
assert ordem_e_progresso(5, 10) == (5, 10)
assert ordem_e_progresso(20, 15) == (15, 20)
assert ordem_e_progresso(4, 4) == (4, 4) # Teste LIMÍTROFE
assert ordem_e_progresso(-2, -8) == (-8, -2) # Teste Valores NEGATIVOS
