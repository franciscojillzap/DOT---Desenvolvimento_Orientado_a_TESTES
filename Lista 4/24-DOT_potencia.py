'''
24. Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula
e retorna Xz. (sem utilizar funções ou operadores de potência prontos)
'''

def potencia(x, z):
    if not isinstance(x, (int, float)) or not isinstance(z, int):
        return Exception

    if z == 0:
        return 1.0 if isinstance(x, float) else 1

    # Tratamento para expoente negativo
    expoente_positivo = abs(z)
    
    # Lógica de cálculo sem usar ** ou pow()
    resultado = 1
    for _ in range(expoente_positivo):
        resultado *= x

    if z < 0:
        return round(1 / resultado, 4)

    return resultado

# Testes de Valores Inválidos
assert potencia("2", 3) == Exception
assert potencia(2, "3") == Exception
assert potencia(2, 2.5) == Exception # Expoente não inteiro

# Testes de Valores Limítrofes e Classes Válidas
assert potencia(5, 0) == 1              # Limítrofe: X^0 = 1
assert potencia(2, 1) == 2              # Limítrofe: X^1 = X
assert potencia(2, 3) == 8              # Classe válida: 2 * 2 * 2 = 8
assert potencia(-3, 2) == 9             # Base negativa com expoente par
assert potencia(-3, 3) == -27           # Base negativa com expoente ímpar
assert potencia(2, -2) == 0.25          # Expoente negativo: 1 / 4 = 0.25

print("Questão 24 ok!")