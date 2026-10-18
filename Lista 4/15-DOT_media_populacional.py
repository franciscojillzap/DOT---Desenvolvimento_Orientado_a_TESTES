'''
15. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
coletando dados sobre o salário e número de filhos. Faça uma função que leia
esses dados para um número não determinado de pessoas e retorne a média de
salário da população, a média do número de filhos, o maior salário e o percentual
de pessoas com salário até R$ 350,00.
'''

def pesquisa_populacao(dados):
    if not isinstance(dados, list) or len(dados) == 0:
        return Exception

    total_salario = 0
    total_filhos = 0
    maior_salario = 0
    qtd_ate_350 = 0

    for item in dados:
        if not isinstance(item, tuple) or len(item) != 2:
            return Exception
        sal, filhos = item
        if not isinstance(sal, (int, float)) or not isinstance(filhos, int) or sal < 0 or filhos < 0:
            return Exception

        total_salario += sal
        total_filhos += filhos
        if sal > maior_salario:
            maior_salario = sal
        if sal <= 350.0:
            qtd_ate_350 += 1

    total_pessoas = len(dados)
    media_sal = round(total_salario / total_pessoas, 2)
    media_filhos = round(total_filhos / total_pessoas, 2)
    perc_ate_350 = round((qtd_ate_350 / total_pessoas) * 100, 2)

    return (media_sal, media_filhos, maior_salario, perc_ate_350)

# Testes de Entradas Inválidas
assert pesquisa_populacao([]) == Exception
assert pesquisa_populacao("invalid") == Exception
assert pesquisa_populacao([(-100, 2)]) == Exception

# Testes de Classes Válidas (incluindo valores limítrofes R$ 350,00)
dados_teste = [(200.0, 1), (350.0, 2), (1000.0, 3)]
# Médias: Salário = (200+350+1000)/3 = 516.67; Filhos = (1+2+3)/3 = 2.0; Maior = 1000.0; % <= 350 = (2/3)*100 = 66.67
assert pesquisa_populacao(dados_teste) == (516.67, 2.0, 1000.0, 66.67)
print("Questão 15 ok!")