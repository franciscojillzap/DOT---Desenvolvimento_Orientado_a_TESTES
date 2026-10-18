'''
11-Faça uma função que recebe, por parâmetro, a altura e o sexo de uma pessoa e retorna o seu peso ideal. 
	# Para homens, usar a fórmula peso ideal = 72.7 * altura - 58
	# Para mulheres, peso ideal = 62.1 * altura - 44.7.
'''

def peso_ideal(altura, sexo):
	if not isinstance(altura, (int, float)) or altura <= 0:
		return Exception
	if sexo not in ["M", "F", "m", "f"]:
		return Exception

	sexo = sexo.upper()

	if sexo == "M":
		return round(72.7 * altura - 58, 2)
	else:
		return round(62.1 * altura - 44.7, 2)

# Teste de valores INVÁLIDOS & IMPROVÁVEIS
assert peso_ideal(-1.83, "M") == Exception # Altura é NEGATIVO
assert peso_ideal(0, "F") == Exception # Altura igual a ZERO
assert peso_ideal("1.83", "M") == Exception # Altura é uma STRING
assert peso_ideal(1.83, "A") == Exception # Sexo nem Masculino, nem Feminino

# Teste com valores VÁLIDOS
assert peso_ideal(1.83, "M") == round(72.7 * 1.83 - 58, 2) # Peso Ideal -> 75.04
assert peso_ideal(1.64, "F") == round(62.1 * 1.64 - 44.7, 2) # Peso Ideal -> 57.14
assert peso_ideal(1.90, "m") == round(72.7 * 1.90 - 58, 2) # Peso Ideal -> 80.13
