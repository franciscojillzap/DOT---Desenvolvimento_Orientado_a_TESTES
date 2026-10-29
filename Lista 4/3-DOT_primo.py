'''
Questão 3: 3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário.
'''

def ver_primo(n1):
    if type(n1) != int or n1 == n1 < 2:
        return Exception
    
    for i in range(2, n1):
        if n1 % i == 0:
            return False
    return True

# Testes
assert ver_primo(2) == True
assert ver_primo(1) == Exception
assert ver_primo(4) == False
assert ver_primo(9) == False
assert ver_primo(1) == Exception
assert ver_primo(0) == Exception
assert ver_primo(-5) == Exception
assert ver_primo("abc") == Exception

print('Testes ok!')