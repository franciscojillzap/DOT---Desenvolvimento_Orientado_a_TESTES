'''
Questão 18 – Conversão de segundos
Crie converter_segundos(total), que converta um inteiro não negativo em uma 
tupla (horas, minutos, segundos). Para valores negativos, lance ValueError.

assert converter_segundos(3661) == (1, 1, 1)
assert converter_segundos(60) == (0, 1, 0)
'''

def converter_segundos(total):
	if type(total) != int or total < 0:
		return "O valor deve ser um inteiro não negativo"

	horas = total // 3600 # 1 hora --> 3600 segundos
	sobra = total % 3600
	minutos = sobra // 60 # 1 minutos --> 60 segundos
	segundos = sobra % 60

	tempo = (horas, minutos, segundos)

	return tempo

assert converter_segundos("mil duzentos e sessenta") == "O valor deve ser um inteiro não negativo"
assert converter_segundos(-1260) == "O valor deve ser um inteiro não negativo"

assert converter_segundos(3661) == (1, 1, 1)
assert converter_segundos(60) == (0, 1, 0)

print("Todos os testes OK!")