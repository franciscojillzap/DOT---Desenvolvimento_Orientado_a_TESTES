'''
Questão 7 – Palíndromo
Implemente eh_palindromo(texto), ignorando espaços, pontuação, acentos e caixa.
'''

# Palíndromo: palavra, frase ou número que lido de trás pra frente permanece igual
def eh_palindromo(texto):
	if type(texto) != str:
		return Exception

	texto_invertido = texto[::-1]

	if texto != texto_invertido:
		return False

	return True

assert eh_palindromo("arara") == True
assert eh_palindromo("Python") == False

# Valores inválidos
assert eh_palindromo(10) == Exception

print("Todos os testes OK!")
