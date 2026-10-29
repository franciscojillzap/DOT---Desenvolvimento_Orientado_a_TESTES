'''
Questão 9: Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
ímpar. A função deve retornar um valor booleano.
'''

def impar_par(n1):
    if type(n1) != int :
        return Exception
    if n1 %2 == 0:
        return True
    else:
        return False
    
#TEstes
assert impar_par(8) == True
assert impar_par(9) == False
assert impar_par(0) == True
assert impar_par(-4) == True
assert impar_par(-7) == False
assert impar_par(6.2) == Exception
assert impar_par(-3.5) == Exception
assert impar_par('abc') == Exception
assert impar_par('') == Exception
assert impar_par(3) == False
assert impar_par(5) == False
assert impar_par(24) == True

print('Testes OK!!')