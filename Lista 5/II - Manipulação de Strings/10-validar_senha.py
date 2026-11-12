'''
Questão 10 – Validar senha
Implemente validar_senha(senha). Exija pelo menos oito caracteres, uma maiúscula, um número e um caractere especial.
'''

import re

def validar_senha(senha):
    # 1. Garante que a entrada seja uma string válida
    if not isinstance(senha, str):
        return False
        
    # 2. Expressão regular com todos os critérios solicitados:
    # (?=.*[A-Z])     -> Pelo menos uma letra maiúscula
    # (?=.*\d)        -> Pelo menos um número
    # (?=.*[^A-Za-z0-9]) -> Pelo menos um caractere especial (qualquer um que não seja letra ou número)
    # .{8,}           -> No mínimo 8 caracteres no total
    padrao = r"^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"
    
    # 3. re.match retorna um objeto se a senha for válida, ou None se falhar.
    # Transformamos o resultado em Booleano (True ou False).
    return bool(re.match(padrao, senha))

# --- Casos de teste do enunciado ---
assert validar_senha("Senha123!") == True
assert validar_senha("abc123") == False

# --- Casos de teste adicionais para garantir o funcionamento ---
assert validar_senha("senha123!") == False  # Falta maiúscula
assert validar_senha("Senha!!!") == False   # Falta número
assert validar_senha("Senha123") == False   # Falta caractere especial
assert validar_senha("Se1!") == False       # Menor que 8 caracteres

print("Todos os testes OK!")
