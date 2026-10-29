"""
Questão 10: 10. Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:
Nota Conceito:

de 0,0 a 4,9 D
de 5,0 a 6,9 C
de 7,0 a 8,9 B
de 9,0 a 10,0A
"""

def conceito(nota):
    if type(nota) != int and type(nota) != float:
        return Exception

    if nota < 0 or nota > 10:
        return Exception
    
    if nota < 5:
        return 'D'
    elif nota <7:
        return 'C'
    elif nota <9:
        return 'B'
    else:
        return 'A'

# TESTES

# Testes de valores inválidos
assert conceito(-1) == Exception
assert conceito(11) == Exception
assert conceito(-0.5) == Exception
assert conceito("abc") == Exception
assert conceito("") == Exception

# Conceito D: de 0 até 4,9
assert conceito(0) == "D"
assert conceito(2) == "D"
assert conceito(4.9) == "D"

# Conceito C: de 5 até 6,9
assert conceito(5) == "C"
assert conceito(6) == "C"
assert conceito(6.9) == "C"

# Conceito B: de 7 até 8,9
assert conceito(7) == "B"
assert conceito(8) == "B"
assert conceito(8.9) == "B"

# Conceito A: de 9 até 10
assert conceito(9) == "A"
assert conceito(10) == "A"

print("Testes OK!!")