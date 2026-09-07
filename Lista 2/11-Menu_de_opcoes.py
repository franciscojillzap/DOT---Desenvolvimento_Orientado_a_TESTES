'''
11) Faça um programa que alimente uma lista com um número de posições definidas pelo
usuário.
Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
======MENU========
1)Cadastar nome
2)Pesquisar nome
3)Listar todos os nome
0) Sair do programa
——————–
Digite sua escolha:
'''

def cadastrar_nome(lista, novo_nome):
	lista.append(novo_nome)

	return f"{novo_nome} foi adicionado a lista com sucesso!"

def pesquisar_nome(lista, nome):
	if nome in lista:
		posicao = lista.index(nome)
		return f"{nome} está presente na lista e é o {posicao+1}º nome cadastrado."
	else:
		return f"{nome} não está presente na lista. Use a opção de cadastro para adicioná-lo."

def listar_nomes(lista):
	print("Nomes cadastrados:")
	for nome in lista:
		print(nome)

usuarios = []

while True:
	try:
		
		print('''
======MENU======
1)CADASTRAR nome
2)PESQUISAR nome
3)LISTAR nomes
0)SAIR do programa
''')
		opcao = int(input("Digite sua escolha: "))

		if opcao == 1:
			nome = input("Digite o nome desejado: ")
			print(cadastrar_nome(usuarios, nome))
		elif opcao == 2:
			nome = input("Digite o nome que deseja pesquisar: ")
			print(pesquisar_nome(usuarios, nome))
		elif opcao == 3:
			listar_nomes(usuarios)
		elif opcao == 0:
			print("Encerrando programa...Adeus...")
			break
		else:
			print("A opção escolhida não consta no menu.")

	except ValueError:
		print("Valor inválido. A opção precisa ser um valor númerico de 0 a 3.")