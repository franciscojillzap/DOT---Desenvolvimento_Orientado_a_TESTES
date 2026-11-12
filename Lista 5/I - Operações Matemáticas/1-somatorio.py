'''
Questão 1 – Soma de números
Implemente somar(a, b), retornando a soma. Testes positivos, negativos, zero e decimais.
'''

def somar(a, b):
	if any(not isinstance(x, (int, float)) for x in [a, b]):
		return Exception

	resultado = a + b

	return resultado

# Valores Válidos (Positivos, Negativos, Zero e Decimais)
assert somar(5, 3) == 8 
assert somar(-5, -3) == -8 
assert somar(8, -8) == 0
assert somar(10, 0) == 10 
assert somar(5.5, 4.5) == 10.0

# Valor Improvável
assert somar("A", "B") == Exception

print("Todos os testes OK!")