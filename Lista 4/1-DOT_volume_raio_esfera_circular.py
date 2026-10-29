'''
Questão 1: 1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
seu volume (v = 4/3 * PI * R**3).
'''

def calcular_vol(raio):
    volume = (4/3) * 3.14 * (raio **3)
    return volume

# teste DOT
assert calcular_vol(2) == (4/3) *3.14 * (2**3)
assert calcular_vol(4) == (4/3) *3.14 * (4**3)
assert calcular_vol(0) == 0
assert calcular_vol(1.5) == (4/3) *3.14 * (1.5**3)
assert calcular_vol(-2) == (4/3) *3.14 * (-2**3)

print("A função passou em todos os testes!")