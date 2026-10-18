'''
16. Faça uma função que leia um número não determinado de valores positivos
e retorna a média aritmética dos mesmos.
'''

def media(valores):
    if not isinstance(valores, list) or len(valores) == 0:
        return Exception

    for v in valores:
        if not isinstance(v, (int, float)) or v <= 0: # Exige positivos
            return Exception

    return round(sum(valores) / len(valores), 2)

# Testes de Valores Inválidos ou Improváveis
assert media([]) == Exception
assert media([10, -5, 20]) == Exception # Negativo presente
assert media([10, 0, 20]) == Exception  # Zero presente

# Teste de Classes Válidas
assert media([10, 20, 30]) == 20.0
assert media([5.5, 4.5]) == 5.0

print("Questão 16 ok!")
