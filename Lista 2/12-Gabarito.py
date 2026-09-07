'''
12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
	--Cartão gabarito;
	--Número de alunos da turma;
	--Cartão de respostas para cada aluno, contendo o seu número e suas respostas.
'''

def processar_resultados_prova():
    # Leitura do gabarito (30 questões)
    print("--- Cadastro do Gabarito Oficial ---")
    gabarito = []
    for i in range(1, 31):
        while True:
            resposta = input(f"Resposta da questão {i} (A, B, C, D ou E): ").strip().upper()
            if resposta in ['A', 'B', 'C', 'D', 'E']:
                gabarito.append(resposta)
                break
            print("Resposta inválida! Digite apenas A, B, C, D ou E.")

    # 2. Leitura do número de alunos
    print("\n--- Dados da Turma ---")
    while True:
        try:
            num_alunos = int(input("Digite o número de alunos da turma: "))
            if num_alunos > 0:
                break
            print("O número de alunos deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    # 3. Processamento dos cartões de resposta
    print("\n--- Processamento das Notas ---")
    resultados = []

    for aluno_idx in range(num_alunos):
        print(f"\nDados do aluno {aluno_idx + 1}:")
        numero_aluno = input("Número de matrícula/identificação do aluno: ").strip()
        
        # Leitura das respostas do aluno
        respostas_aluno = []
        for i in range(1, 31):
            while True:
                resp = input(f"Resposta do aluno para a questão {i}: ").strip().upper()
                if resp in ['A', 'B', 'C', 'D', 'E']:
                    respostas_aluno.append(resp)
                    break
                print("Resposta inválida! Digite apenas A, B, C, D ou E.")
        
        # Cálculo dos acertos
        acertos = 0
        for q in range(30):
            if respostas_aluno[q] == gabarito[q]:
                acertos += 1
                
        # Armazena o resultado
        resultados.append({"numero": numero_aluno, "acertos": acertos})

    # 4. Publicação dos resultados
    print("\n--- Resultado da Turma ---")
    print(f"{'Nº do Aluno':<15} | {'Número de Acertos':<17}")
    print("-" * 37)
    for res in resultados:
        print(f"{res['numero']:<15} | {res['acertos']:<17}")

# Executa o programa
if __name__ == "__main__":
    processar_resultados_prova()
