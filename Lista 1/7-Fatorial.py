"""
7. Faça um programa para calcular o Fatorial de um número.
Utilize uma função que recebe como parâmetro de entrada o número a ser calculado
o fatorial e retorna o fatorial deste número.
"""

def fatorial(n):
    resultado = n

    # -1 indica para o loop que ele deve prosseguir em ordem DECRESCENTE
    # N - 1 indica o valor que o índice deve ter inicialmente, sempre um a menos para efetuar o cálculo do fatorial corretamente
    for i in range(n - 1, 0, -1):
        print(f"{resultado} * {i} = {resultado * i}")
        #Guarda o valor da operação acima na variável resultado
        #Esse valor é usado para multiplicar o próximo valor do índice e prosseguir com o cálculo do fatorial
        resultado = resultado * i

while True:
    try:
        print("Vamos calcular o fatorial de um número!")
        numero = int(input("Digite um número: "))

        print(f"O fatorial de {numero}! é:")

        fatorial(numero)

        break
    except ValueError:
        print("O valor precisa corresponder a um número INTEIRO.\n")
