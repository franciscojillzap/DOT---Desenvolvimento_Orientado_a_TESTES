'''
Questão 7: Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo:
Idade Categoria
5 a 7 anos Infantil A
8 a 10 anos Infantil B
11-13 anos Juvenil A
14-17 anos Juvenil B
Maiores de 18 anos
(inclusive)

Adulto
'''

def categoria(idade):
    if type(idade) != int or idade <5:
        return Exception
    
    if idade <=7:
        return "Infantil A"
    elif idade <=10:
        return 'Infantil B'
    elif idade <=13:
        return 'Juvenil A'
    elif idade <=17:
        return 'Juvenil B'
    else:
        return 'Adulto'
    
#TESTES
        
assert categoria(-1) ==  Exception
assert categoria(0) ==  Exception
assert categoria(3) ==  Exception
assert categoria('sla') ==  Exception
assert categoria(2.4) ==  Exception
assert categoria(5) == "Infantil A"
assert categoria(6) == "Infantil A"
assert categoria(7) == "Infantil A"

assert categoria(8) == "Infantil B"
assert categoria(10) == "Infantil B"

assert categoria(11) == "Juvenil A"
assert categoria(13) == "Juvenil A"

assert categoria(14) == "Juvenil B"
assert categoria(17) == "Juvenil B"

assert categoria(18) == "Adulto"
assert categoria(25) == "Adulto"


print('Testes OK!!')
    