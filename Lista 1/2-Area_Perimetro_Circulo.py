#Q2-Escreva um programa que leia o raio de um círculo e faça duas funções:
    #Uma função chamada ÁREA que calcula e retorna a área do círculo
    #Outra função chamada PERÍMETRO que calcula e retorna o perímetro do círculo.

def area_circulo(raio):
    calc_area = round(3.14 * (raio**2),2)
    return f"O cálculo da área desse círculo resulta em {calc_area}."

def perimetro_circulo(raio):
    calc_perimetro = round(3.14 * 2 * raio,2)
    return f"O cálculo do perímetro desse círculo resulta em {calc_perimetro}."

while True:
    try:
        raio = float(input("\nQual o valor do raio do círculo? "))
        if raio == 0:
            print("O raio não pode ser igual a zero. Tente novamente.")
            continue
        elif raio < 0:
            print("O raio não pode ser negativo. Tente novamente.")
            continue
    except:
        print("Por favor, digite um número válido.")
        continue

    print("\nDigite:")
    print("1 - Calcular área")
    print("2 - Calcular perímetro")
    print("3 - Calcular ambos")
    caminho = input("Opção: ").strip()

    if caminho == "1":
        print(area_circulo(raio))
        
        resposta = input("\nDescobrir o valor do perímetro? (S/N): ").strip().upper()
        if resposta == "S":
            print(perimetro_circulo(raio))

    elif caminho == "2":
        print(perimetro_circulo(raio))
        
        resposta = input("\nDescobrir o valor da área? (S/N): ").strip().upper()
        if resposta == "S":
            print(area_circulo(raio))
            
    elif caminho == "3":
        print(area_circulo(raio))
        print(perimetro_circulo(raio))

    else:
        print("Opção inválida.")
        continue

    # Pergunta para decidir se o looping continua ou encerra
    repetir_ou_nao = input("\nDeseja calcular o raio de outro círculo? (S/N): ").strip().upper()
    if repetir_ou_nao == "N":
        print("Programa encerrado. Até breve!")
        break
