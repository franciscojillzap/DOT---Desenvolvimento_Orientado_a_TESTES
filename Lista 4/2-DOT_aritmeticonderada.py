"""Questão 2: 2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma
letra. Se a letra for A o procedimento calcula a média aritmética das notas do
aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
a média calculada.
"""

def notas(n1, n2, n3, letra):
    
    if type(n1) != int or type(n2) != int or type(n3) != int or type(letra) != str:
        return Exception
    
    if letra == "A":
        return (n1+ n2 + n3)/3
    
    elif letra == "P":
        return (n1*5 + n2*3 + n3*2)/10
    
#TESTES
assert notas(3,5,8, 1) == Exception
assert notas(3.2,-5, 8, "P") == Exception
assert notas("x", 6, 10, "A") == Exception
assert notas(4, 5, 8, "P") == 5.1
assert notas(2,3,4, "A") == 3

print("Todos os teste ok!")