'''
Questão 19 – Validação de data
Crie data_valida(dia, mes, ano), retornando 
	# True para datas válidas do calendário gregoriano (ano >= 1)
	# False para as demais, incluindo fevereiro em anos bissextos.

assert data_valida(29, 2, 2024) == True
assert data_valida(29, 2, 2023) == False
'''

# Reaproveitando da Questão 16!
def eh_bissexto(ano):
  return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def data_valida(dia, mes, ano):
  data = (dia, mes, ano)

  # all - garante que todos as variáveis são valores INT
  # any - garante que pelo menos uma variável possui valor INT
  if not all(isinstance(x, int) for x in data):
    return False

  # Validação para ANO e MÊS
  if ano < 1 or not (1 <= mes <= 12):
    return False

  # Máximo de dias para o mês informado
  if mes in (4, 6, 9, 11):
  	# Abril, Junho, Setembro, Novembro
    max_dias = 30 
  elif mes == 2: 
  	# Fevereiro
    max_dias = 29 if eh_bissexto(ano) else 28
  else:
  	# Janeiro, Março, Maio, Julho, Agosto, Outubro, Dezembro
    max_dias = 31

  # Verifica se o dia está dentro do intervalo válido para aquele mês
  return 1 <= dia <= max_dias


# Testes
assert data_valida(29, 2, 2024) == True
assert data_valida(29, 2, 2023) == False
assert data_valida(31, 4, 2026) == False  # Abril só tem 30 dias
assert data_valida(12, 12, 0) == False  # Ano precisa ser >= 1
assert data_valida("doze", "dezembro", 2026) == False

print("Todos os testes OK!")
