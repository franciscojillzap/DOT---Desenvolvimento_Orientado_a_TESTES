'''
Questão 21:  21. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N
e retorna o valor de S.

S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
'''

def calcular_S(n1):
    if type(n1) != int or n1 <=0:
        return Exception
    
    s=0
    for i in range(1, n1 +1):
        s = s + 1/i
    return round(s, 2)

#TESTES
assert calcular_S("abc") == Exception
assert calcular_S('') ==  Exception
assert calcular_S(-12) ==  Exception
assert calcular_S(1.7) == Exception

assert calcular_S(2) == 1.5
assert calcular_S(5) == 2.28
assert calcular_S(9) == 2.83



print("Testes ok!! Questão 21")