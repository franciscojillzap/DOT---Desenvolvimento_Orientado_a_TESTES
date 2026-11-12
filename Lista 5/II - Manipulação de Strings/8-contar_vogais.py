'''
Questão 8 – Contar vogais
Implemente contar_vogais(texto), incluindo vogais acentuadas.
'''

def contar_vogais(texto):
	if type(texto) != str:
		return Exception

	vogais = [
		"a", "á", "à", "ã", "â",
		"e", "é", "è", "ê",
		"i", "í", "ì", "î",
		"o", "ó", "ò", "õ", "ô",
		"u", "ú", "ù", "û"
	]

	total = 0

	for caractere in texto.lower():
		if caractere in vogais:
			total += 1

	return total

# Valores Válidos
assert contar_vogais("Python") == 1
assert contar_vogais("troca") == 2
assert contar_vogais("BANANA") == 3
assert contar_vogais("ouroboros") == 5

# Valores Inválidos
assert contar_vogais(10) == Exception

print("Todos os testes OK!")
