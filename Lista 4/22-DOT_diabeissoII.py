'''
Questão 22: Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.

S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!
'''

def calcular_s(n1):
    if type(n1) != int or n1 <=0:
            return Exception
        
    s =1
    fatorial=1
    
    for i in range(1, n1 +1):
        fatorial = fatorial*i
        s = s+1 / fatorial
        
    return round(s, 2)

#Testes
assert calcular_s('.da') == Exception
assert calcular_s(-12) == Exception
assert calcular_s(-1.4) == Exception
assert calcular_s(5.1) == Exception

assert calcular_s(1) == 2
assert calcular_s(3) == 2.67
assert calcular_s(9) == 2.72
assert calcular_s(20) == 2.72

print('TEstes OK!! Questão 22')