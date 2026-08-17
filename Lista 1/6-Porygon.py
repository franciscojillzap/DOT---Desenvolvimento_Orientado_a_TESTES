"""
6-Escreva um programa para ler o número de lados de um polígono e a medida do lado (em cm). 
Receba como parâmetro o número de lados e a medida do lado, calcule e imprima o seguinte:
    Se o número de lados for 3, escrever TRIÂNGULO e o valor do seu perímetro.
    Se o número de lados for 4, escrever QUADRADO e o valor da sua área.
    Se o número de lados for 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.
"""

def operacao_poligonal(l):
    n_lados = len(l)

    if n_lados == 3:
        perimetro = sum(l)
        return f"Este polígono é um TRIÂNGULO, seu perímetro é igual a: {perimetro}cm²."
    elif n_lados == 4:
        area = l[1] * l[2]
        return f"Este polígono é um QUADRADO, sua área é igual a: {area}cm²."
    elif n_lados == 5:
        return "Este polígono é um PENTÁGONO."
    else:
        return f"Polígono de {n_lados} lados ainda não foi catalogado."

while True:
    try:
        #Conterá todos os valores correspondentes aos lados do polígono.
        lista_lados = []

        print("Pense em um polígono...")
        n_lados = int(input("Quantos lados ele possui? "))

        for i in range(n_lados):
            lado = float(input(f"Valor do {i+1}º lado: "))
            lista_lados.append(lado)

        print(operacao_poligonal(lista_lados))

        break
    except ValueError:
        print("Insira um valor válido.\n")
