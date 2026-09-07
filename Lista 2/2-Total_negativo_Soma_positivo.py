'''
2) Faça um programa que grave uma lista com dez números reais e:
    Calcule e mostre a quantidade de números negativos,
    Calcule a soma dos números positivos dessa lista.
'''
from random import randint

max_lista = 10

def gravar_lista():
    lista = []

    for i in range(max_lista):
        numero = randint(-100, 100)
        lista.append(numero)

    return lista

def qtd_negativo(lista):
    lista_negativo = []

    for i in range(len(lista)):
        if lista[i] < 0:
            lista_negativo.append(lista[i])

    return f"A lista contém {len(lista_negativo)} números negativos."

def soma_positivo(lista):
    lista_positivo = []

    for i in range(len(lista)):
        if lista[i] > 0:
            lista_positivo.append(lista[i])

    return f"A soma dos números positivos da lista corresponde a {sum(lista_positivo)}."

lista_bacana = gravar_lista()
print(lista_bacana)
print(qtd_negativo(lista_bacana))
print(soma_positivo(lista_bacana))