'''
10. Escreva um programa composto de uma função Max e o programa principal como segue:
	a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. 
		# Se forem iguais retorna qualquer um deles;
	b) O programa principal lê 4 séries de 4 números a, b. 
		# Para cada série lida imprime o maior dos quatro números usando a função Max.
'''

def Max(n1, n2):
	maior_numero = max(n1, n2)
	return maior_numero

print("Verificar o maior número dentro da série")

for i in range(1, 5):
	print(f"{i}ª Série:\n")

	while True:
		try:
			a = int(input("Digite o valor do 1º número: "))
			b = int(input("Digite o valor do 2º número: "))
			c = int(input("Digite o valor do 3º número: "))
			d = int(input("Digite o valor do 4º número: "))

			vencedor1 = Max(a,b)
			vencedor2 = Max(c,d)

			maior_de_todos = Max(vencedor1, vencedor2)

			print(f"O maior número dentro da série {i} é: {maior_de_todos}\n")

			break
		except ValueError:
			print("Entrada inválida. Apenas números inteiros permitidos.\n")

print("Programa finalizado.")