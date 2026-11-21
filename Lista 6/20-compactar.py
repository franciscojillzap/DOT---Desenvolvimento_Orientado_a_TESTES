'''
Questão 20 – Compactação de caracteres consecutivos
Crie compactar(texto), substituindo cada sequência consecutiva de caracteres iguais pelo caractere
seguido de sua contagem. A comparação diferencia maiúsculas e minúsculas.

assert compactar("aaabbc") == a3b2c1
assert compactar("AB") == "A1B1"
'''

def compactar(texto):
  if type(texto) != str:
    return Exception

  # Caso borda: se o texto for vazio "", retorna ""
  if texto == "":
    return ""

  resultado = ""
  contagem = 1

  # Começamos do índice 1 (segunda letra) até o final da string
  for i in range(1, len(texto)):
    if texto[i] == texto[i - 1]:
      # Se a letra atual for igual à anterior, aumente a contagem
      contagem += 1
    else:
      # Se mudou, junte a letra anterior (texto[i - 1]) + str(contagem) no resultado
      resultado += (texto[i - 1] + str(contagem))
      # Reinicie a contagem para 1
      contagem = 1

  # Não esqueça de adicionar o último grupo que ficou pendente após o loop!
  resultado += texto[-1] + str(contagem)

  return resultado

assert compactar(10) == Exception
assert compactar(["abc"]) == Exception

assert compactar("aaabbc") == "a3b2c1"
assert compactar("AB") == "A1B1"

assert compactar("aabbcdd") == "a2b2c1d2"

assert compactar("") == ""  # Testa texto vazio
assert compactar("aA") == "a1A1"  # Testa maiúscula vs minúscula

print("Todos os testes OK!")