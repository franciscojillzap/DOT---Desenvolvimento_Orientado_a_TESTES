'''
25. Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o
seu fatorial.
'''

def fatorial(n):
    # Validação de Tipos e Valores Inválidos/Negativos
    if type(n) != int or n < 0:
        return Exception

    if n == 0 or n == 1:
        return 1

    resultado = 1

    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Testes de Valores Inválidos e Improváveis
assert fatorial(-5) == Exception
assert fatorial(3.14) == Exception
assert fatorial("5") == Exception

# Testes de Valores Limítrofes
assert fatorial(0) == 1 # Limítrofe: 0! = 1
assert fatorial(1) == 1 # Limítrofe: 1! = 1

# Testes de Classes Válidas
assert fatorial(3) == 6 # 3 * 2 * 1 = 6
assert fatorial(5) == 120 # 5 * 4 * 3 * 2 * 1 = 120

print("Questão 25 ok!")