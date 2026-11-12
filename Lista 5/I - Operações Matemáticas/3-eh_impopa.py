'''
Questão 3 – Número par
Implemente eh_par(numero), retornando True para inteiros pares e False para ímpares.
'''

def eh_par(numero):
	if type(numero) != int and numero < 0:
		return Exception

	if numero % 2 == 0:
		return True
	else:
		return False

# Valores Válidos (Pares e Ímpares)
assert eh_par(8) == True
assert eh_par(7) == False

# Valor Limítrofe
assert eh_par(0) == True

# Valores Improváveis e Inválidos
assert eh_par("oito") == Exception
assert eh_par(-1) == Exception