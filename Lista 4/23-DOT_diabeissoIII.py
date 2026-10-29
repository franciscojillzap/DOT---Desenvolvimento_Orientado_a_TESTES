'''
Questão 23:Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3)
'''
def calcular_s(n1):
    if type(n1) != int or n1 <=0:
            return Exception
        
    s =0
    for i in range(1, n1 +1):
        s= s + (i**2 + 1) / (i+3)

    return round(s, 2)

#TESTES OK
assert calcular_s('abcde') == Exception
assert calcular_s(-12) == Exception
assert calcular_s(0) == Exception
assert calcular_s(5.1) == Exception

assert calcular_s(1) == 0.5
assert calcular_s(8) == 23.87
assert calcular_s(16) == 105.14
print("Testes OK!! QUestão 23")
