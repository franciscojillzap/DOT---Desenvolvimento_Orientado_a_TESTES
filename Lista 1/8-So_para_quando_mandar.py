'''
8-Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. 
	# Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. 
	# Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. 
	# O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
'''

def cubo(n):
	resultado = n

	for i in range(2):
		print(f"{resultado} * {n} = {resultado * n}")
		resultado = resultado * n

	return f"O valor de {n}³ é: {resultado}"

def ler_caractere():
	while True:
		prosseguir = input("\nDeseja continuar? (S/N) ").upper()[0]

		if prosseguir in ["S", "N"]:
			return prosseguir
		else:
			print("Caractere inválido. Digite novamente.")

continuar = "S"

while continuar == "S":
	try:
		print("\nCalcular o valor do cubo de um número!")
		numero = int(input("Digite um número: "))

		print(cubo(numero))

		continuar = ler_caractere()

		if continuar == "N":
			print("Encerrando programa...")
			break
	except ValueError:
		print("O valor digitado deve ser um número inteiro.")