'''
19. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o número de divisores desse valor.
'''

def divisores(n):
	if type(n) != int or n <= 0:
		return Exception

	divisores = []

	for div in range(1, n+1):
		if n % div == 0:
			divisores.append(div)

	total_div = len(divisores)

	return total_div

# Testes com valores INVÁLIDOS
assert divisores(0) == Exception
assert divisores(-1) == Exception
assert divisores("1") == Exception

# Testes com valores VÁLIDOS
assert divisores(5) == 2 # 1, 5
assert divisores(10) == 4 # 1, 2, 5, 10
assert divisores(15) == 4 # 1, 3, 5, 15

print("Questão 19 ok!")
