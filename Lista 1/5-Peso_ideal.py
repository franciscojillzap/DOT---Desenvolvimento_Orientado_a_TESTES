
"""
5. Faça um programa que leia a altura e o sexo (1:feminino 2:masculino) de uma pessoa. 
Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
    para homens : (72.7 * h) – 58
    para mulheres : (62.1 * h) – 44.7
"""

def peso_ideal(s, h):
    if s == 1:
        peso_ideal_mulher = round((62.1 * h) - 44.7)
        return peso_ideal_mulher
    if s == 2:
        peso_ideal_homem = round((72.7 * h) - 58, 2)
        return peso_ideal_homem

while True:
    try:
        sexo = int(input("Digite seu sexo (1-feminino 2-masculino): "))
        altura = float(input("Digite sua altura: "))

        peso = peso_ideal(sexo, altura)

        if sexo != 1 and sexo != 2:
            sexo = int(input("\nSelecione um dos sexos disponíveis: "))
            peso = peso_ideal(sexo, altura)
        if sexo == 1:
            print(f"Como mulher, seu peso ideal é: {peso}kg")
        elif sexo == 2:
            print(f"Como homem, seu peso ideal é: {peso}kg")

        break
    except ValueError:
        print("É preciso inserir um valor válido para altura.\n")
