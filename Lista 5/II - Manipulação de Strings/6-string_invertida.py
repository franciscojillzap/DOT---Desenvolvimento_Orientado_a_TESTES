'''
Questão 6 – Inverter uma string
Implemente inverter(texto), retornando a string invertida.
'''

def inverter(texto):
	if type(texto) != str:
		return Exception

	# Maneira 1 - Fatiamento de String
	texto_invertido = texto[::-1]

	# Maneira 2 - Método REVERSE
	texto.reverse()

	# Maneira 3 - Usando FOR
	texto_trocado = ""

	for caractere in texto:
		texto_trocado = caractere + texto_trocado

	return texto_trocado

assert inverter(10) == Exception
assert inverter("Python") == "nohtyP"
assert inverter("abc") == "cba"
assert inverter("a") == "a"
assert inverter("") == ""

print("Todos os testes OK!")