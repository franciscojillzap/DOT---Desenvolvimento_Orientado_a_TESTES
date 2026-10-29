'''
Questão 8: 8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano.
'''
def pos_neg(n1):
    if type(n1) != int:
        return Exception
    
    if n1 >0:
        return True
    else:
        return False
    
# Testes 
assert pos_neg(1) == True
assert pos_neg(12030) == True
assert pos_neg(1.5) == Exception
assert pos_neg(-5.2) == Exception
assert pos_neg(0) == False
assert pos_neg('abcdes') == Exception
assert pos_neg(-250) == False
assert pos_neg(4) == True
assert pos_neg(15) == True
assert pos_neg(-99) == False


print('Testes OK!!')
