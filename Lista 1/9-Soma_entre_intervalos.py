'''
9-Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada 
e retorna a soma de todos os números inteiros contidos no intervalo [n1,n2]. 
	# Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.
'''

def calculo_intervalo(n1, n2):
	inicio = min(n1, n2)
	fim = max(n1, n2)

	soma = 0
	texto_calculo = ""

	for item in range(inicio, fim + 1):
		soma += item

		# Se for o primeiro número, apenas adiciona ele ao texto
		if item == inicio:
			texto_calculo += str(item)
		# Para os próximos números, adiciona um " + " antes do número
		else:
			texto_calculo += " + " + str(item)

	print(f"\nCálculo: {texto_calculo}")
	return soma

while True:
	try:
		print("Realizar soma com valores dentro de um intervalo.")
		numero1 = int(input("Digite o número inicial: "))
		numero2 = int(input("Digite o número final: "))

		total = calculo_intervalo(numero1, numero2)
		print(f"Resultado da soma entre os valores: {total}")

		break
	except ValueError:
		print("Os valores estão fora do padrão esperado. Tente digitar um número inteiro.")