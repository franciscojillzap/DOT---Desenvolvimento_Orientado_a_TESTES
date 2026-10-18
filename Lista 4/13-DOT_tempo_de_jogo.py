'''
13. Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
O procedimento deve retornar, também por parâmetro, a duração do jogo em
horas e minutos, considerando que o tempo máximo de duração de um jogo é
de 24 horas e que o jogo pode começar em um dia e terminar no outro.
'''

def duracao_jogo(h_ini, m_ini, h_fim, m_fim):
    if any(type(x) != int for x in [h_ini, m_ini, h_fim, m_fim]):
        return Exception

    if not (0 <= h_ini <= 23 and 0 <= h_fim <= 23 and 0 <= m_ini <= 59 and 0 <= m_fim <= 59):
        return Exception

    inicio = h_ini * 60 + m_ini
    fim = h_fim * 60 + m_fim

    if fim <= inicio:
        fim += 1440  # 24h * 60min

    duracao = fim - inicio
    return (duracao // 60, duracao % 60)

# Bloco Principal de Testes
assert duracao_jogo("10", 0, 12, 0) == Exception
assert duracao_jogo(24, 0, 10, 0) == Exception
assert duracao_jogo(10, 60, 11, 0) == Exception
assert duracao_jogo(-1, 0, 10, 0) == Exception
assert duracao_jogo(14, 30, 16, 45) == (2, 15)
assert duracao_jogo(22, 10, 2, 40) == (4, 30)
assert duracao_jogo(10, 0, 10, 0) == (24, 0)

print("Todos os testes ok!")