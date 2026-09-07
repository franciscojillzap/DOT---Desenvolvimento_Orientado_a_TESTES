'''
3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da leitura.
'''

from random import randint

def ordem_inversa(lista):
    lista.reverse()

    return lista

lista_original = []

max_lista = int(input("Digite o número de elementos que a lista deve conter: "))

for i in range(max_lista):
    numero = randint(0, 100)
    lista_original.append(numero)

print(f"Esta é a lista original criada: {lista_original}")
print(f"Esta é a lista modificada (inversa): {ordem_inversa(lista_original)}")