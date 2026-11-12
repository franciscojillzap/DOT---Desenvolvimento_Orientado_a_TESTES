'''
Questão 4 – Fatorial
Implemente fatorial(n) para inteiros não negativos.
'''

def fatorial(n):
	if type(n) != int and n < 0:
		return Exception

	fat = 1

	for i in range(1, n+1):
		fat = fat * i

	return fat

# Valores Válidos
assert fatorial(0) == 1
assert fatorial(1) == 1
assert fatorial(5) == 120

# Valores Inválidos e Improváveis
assert fatorial("zero") == Exception
assert fatorial(-3) == Exception
