"""
4-Escreva um programa para ler as notas das duas avaliações de um aluno no semestre.
Faça um procedimento que receba as duas notas e calcule e escreva a média semestral
    Mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado
    (Considere 6.0 a média mínima para aprovação).
"""

def calculo_media(n):
    lista = n
    media = sum(lista) / len(lista)
    return media

while True:
    try:
        print("Vamos avaliar seu desempenho!")

        notas = []

        for i in range(2):
            nota = float(input(f"Digite a {i+1}ª nota: "))
            notas.append(nota)

        resultado = calculo_media(notas)

        if resultado == 10:
            print(f"Sua nota foi {resultado}. Que aluno exemplar! PARABÉNS!")
        elif resultado >= 6:
            print(f"Sua nota foi {resultado}. PARABÉNS! Você foi aprovado!")
        else:
            print(f"Sua nota foi {resultado}. Terrível. Nos encontraremos novamente próximo semestre.")

        break

    except ValueError:
        print("Insira a nota corretamente.\n")
