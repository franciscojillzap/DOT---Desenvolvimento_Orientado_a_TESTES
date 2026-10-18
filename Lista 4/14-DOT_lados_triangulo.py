'''
14. Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se
esses valores podem ser os comprimentos dos lados de um triângulo e, neste
caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um
triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento
de cada lado de um triângulo é menor do que a soma do comprimento dos outros
dois lados. O procedimento deve identificar o tipo de triângulo formado
observando as seguintes definições:
	# Equilátero: os comprimentos dos 3 lados são iguais.
	# Isósceles: os comprimentos de 2 lados são iguais.
	# Escaleno: os comprimentos dos 3 lados são diferentes.
'''

def tipo_triangulo(x, y, z):
    if not all(isinstance(v, (int, float)) for v in [x, y, z]) or x <= 0 or y <= 0 or z <= 0:
        return Exception

    # o comprimento de cada lado do triângulo é menor do que a soma do comprimento dos outros dois lados.
    if not (x < y + z and y < x + z and z < x + y):
        return False

    if x == y == z:
        return "Equilátero" # os comprimentos dos 3 lados são iguais.
    elif x == y or y == z or x == z:
        return "Isósceles" # os comprimentos de 2 lados são iguais.
    else:
        return "Escaleno" # os comprimentos dos 3 lados são diferentes.

# Testes de Valores Inválidos
assert tipo_triangulo(-3, 4, 5) == Exception
assert tipo_triangulo(0, 4, 5) == Exception
assert tipo_triangulo("3", 4, 5) == Exception

# Testes de Não-Triângulo
assert tipo_triangulo(1, 2, 3) == False # Viola propriedade (1 < 2+3 mas não forma área)
assert tipo_triangulo(10, 2, 2) == False

# Testes de Classes Válidas
assert tipo_triangulo(5, 5, 5) == "Equilátero"
assert tipo_triangulo(5, 5, 3) == "Isósceles"
assert tipo_triangulo(3, 4, 5) == "Escaleno"

print("Questão 14 ok!")