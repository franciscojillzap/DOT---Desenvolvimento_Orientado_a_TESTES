"""
3-Escreva um programa para ler uma temperatura em graus Fahrenheit. 
Faça uma função para calcular e retornar o valor em graus Celsius.
    Fórmula: Celcius = ((F-32)/9)*5
"""

def converter_para_celcius(F):
    celcius = round(((F-32)/9)*5, 2)
    return celcius

while True:
    try:
        temperatura = float(input("Digite um valor para temperatura em fahrenheit: "))
        resultado_conversao = converter_para_celcius(temperatura)

        print(f"Este é o valor equivalente a temperatura em graus Celcius: {resultado_conversao}")

        break
    except ValueError:
        print("Insira um valor válido.\n")
