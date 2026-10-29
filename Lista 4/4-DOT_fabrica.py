'''
Questão 4: Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos.
'''

def tempo_duracao(segundos):
    if type(segundos) != int or segundos <0:
        return Exception
    
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundo_restante = (segundos % 3600) % 60
    
    return f'{horas}:{minutos}:{segundo_restante}'

# Testes
assert tempo_duracao(-60) == Exception
assert tempo_duracao('abc') == Exception
assert tempo_duracao('') == Exception
assert tempo_duracao(2.5) == Exception
assert tempo_duracao(3600) == '1:0:0'
assert tempo_duracao(3672) == '1:1:12'
assert tempo_duracao(7200) == '2:0:0'

print('Testes OK!!')