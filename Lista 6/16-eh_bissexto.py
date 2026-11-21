'''
Questão 16 – Ano bissexto
Crie eh_bissexto(ano), seguindo as regras do calendário gregoriano: 
	# divisível por 4, exceto séculos não divisíveis por 400.

assert eh_bissexto(2000) == True
assert eh_bissexto(1900) == False
'''

def eh_bissexto(ano):
	if type(ano) != int or ano < 0:
		return Exception

	if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
		return True
	else:
		return False

assert eh_bissexto("dois mil e vinte") == Exception
assert eh_bissexto(-2020) == Exception

assert eh_bissexto(2000) == True
assert eh_bissexto(1900) == False

assert eh_bissexto(2024) == True

print("Todos os testes OK!")