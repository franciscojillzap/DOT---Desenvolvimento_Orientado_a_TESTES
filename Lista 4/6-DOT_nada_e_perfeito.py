'''
Questão 6: Faça uma função que verifique se um valor é cell_perfeito ou não. Um valor é dito
cell_perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é cell_perfeito, 6 =  1+ 2 + 3, que são seus divisores). A função deve retornar
um valor booleano.
'''

def cell_perfeito(n1):
    if type(n1) != int or n1 <=0:
        return Exception
    
    soma = 0
    for i in range(1, n1):
        if n1 % i ==0:
            soma = soma +i
    return soma == n1

# Testando

assert cell_perfeito(6) == True
assert cell_perfeito(28) == True
assert cell_perfeito(496) == True
assert cell_perfeito(1) == False
assert cell_perfeito(2) == False
assert cell_perfeito(10) == False
assert cell_perfeito(12) == False

assert cell_perfeito(0) == Exception
assert cell_perfeito(-6) == Exception
assert cell_perfeito("abc") == Exception
assert cell_perfeito(2.5) == Exception

print('Testes OK!!')