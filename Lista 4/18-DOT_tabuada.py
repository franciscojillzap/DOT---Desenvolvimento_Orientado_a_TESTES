'''
18. Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve
a tabuada de 1 até N. Mostre a tabuada na forma:
	# 1 x N = N
	# 2 x N = 2N
	# ...
	# N x N = N2
'''

def tabuada(n):
	if type(n) != int or n <= 0:
		return Exception

	tabuada = []

	for i in range(1, n+1):
		tabuada.append(f"{n} x {i} = {n*i}")

	return tabuada

# Testes com valores INVÁLIDOS
assert tabuada(-1) == Exception
assert tabuada(0) == Exception
assert tabuada("1") == Exception

# Testes com valores VÁLIDOS
assert tabuada(1) == ["1 x 1 = 1"]
assert tabuada(2) == ["2 x 1 = 2", "2 x 2 = 4"]

print("Questão 18 ok!")
