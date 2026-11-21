'''
Questão 17 – Classificação de triângulos
Crie tipo_triangulo(a, b, c), que retorne Equilatero, Isosceles, Escaleno ou Invalido,
considerando comprimentos positivos e a desigualdade triangular.

assert tipo_triangulo(3, 3, 3) == Equilatero
assert tipo_triangulo(1, 2, 3) == Invalido
'''

def tipo_triangulo(a, b, c):
	lados = (a, b, c)

	if not all(isinstance(x, (int, float)) for x in lados):
		return Exception

	if any(x <= 0 for x in lados):
		return Exception

	# Desigualdade Triangular - Verifica se os lados formam um triângulo
	# A soma de dois lados deve ser maior que o terceiro
	if not (a + b > c and a + c > b and b + c > a):
		return "Inválido"

	if a == b == c:
		return "Equilátero" # 3 lados iguais
	elif a == b or a == c or b == c:
		return "Isósceles" # 2 lados iguais
	else:
		return "Escaleno" # 3 lados diferentes

assert tipo_triangulo("tres", "cinco", "nove") == Exception
assert tipo_triangulo(-3, -5, -9) == Exception

assert tipo_triangulo(3, 3, 3) == "Equilátero"
assert tipo_triangulo(3, 3, 2) == "Isósceles"
assert tipo_triangulo(3, 4, 5) == "Escaleno"
assert tipo_triangulo(1, 2, 3) == "Inválido"

print("Todos os testes OK!")