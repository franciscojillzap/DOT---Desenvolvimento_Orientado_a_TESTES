'''
17. Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.
'''

def maior_menor(valores):
    # Validação de tamanho da lista e tipo de elementos
    if not isinstance(valores, list) or len(valores) != 50:
        return Exception
    if any(type(x) != int for x in valores):
        return Exception

    return (max(valores), min(valores))

# Testes de Valores Inválidos
assert maior_menor([1] * 49) == Exception # Tamanho incorreto
assert maior_menor([1.5] + [1] * 49) == Exception # Tipo incorreto

# Testes de Classes Válidas
lista_valida = list(range(1, 51)) # 1 até 50
assert maior_menor(lista_valida) == (50, 1)

lista_iguais = [7] * 50
assert maior_menor(lista_iguais) == (7, 7) # Limítrofe: todos elementos iguais

print("Questão 17 ok!")
