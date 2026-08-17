#Q1-Faça uma função que recebe um número inteiro por parâmetro:
    #Retorna VERDADEIRO se ele for PAR
    #E FALSO se for ÍMPAR.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        num = int(input("Digite um número: "))
        if par_ou_impar(num):
            print("O número é par.")
        else:
            print("O número é ímpar.")
        break
    except:
        print("Erro: Digite um número inteiro válido!")
