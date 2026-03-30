'''Robert está desenvolvendo um sistema de cadastro para um aplicativo. Toda vez que um novo cliente preenche o formulário, o sistema precisa verificar se o CPF informado é válido. Isso garante que os dados cadastrados sejam verdadeiros e que não haja fraudes.
Objetivo: Desenvolver um programa que receba um número de CPF e informe se ele é válido ou inválido.
Regras: O CPF deve conter 11 dígitos numéricos (com ou sem pontos e traço). O programa deve desconsiderar pontos e traços, avaliando apenas os números. CPFs com todos os dígitos iguais são inválidos. A verificação dos dois últimos dígitos (dígitos verificadores) deve seguir as regras abaixo:
Cálculo do primeiro dígito verificador (10º dígito): Multiplique os 9 primeiros dígitos por pesos de 10 a 2. Some todos os resultados. Calcule: soma % 11. Se o resultado for menor que 2, o dígito é 0. Caso contrário, o dígito é 11 - (soma % 11).
Cálculo do segundo dígito verificador (11º dígito): Multiplique os 10 primeiros dígitos (os 9 iniciais + o primeiro dígito verificador) por pesos de 11 a 2. Repita o mesmo cálculo. Se os dois dígitos calculados forem iguais aos dois últimos dígitos do CPF informado, o CPF é considerado válido. Caso contrário, o CPF é inválido.
'''


import re

# Entrada e limpeza do CPF (remove tudo que não for número)
entrada = input("Digite o CPF para validação: ")
cpf = re.sub(r'\D', '', entrada)

# Regra 1: Verificar se tem 11 dígitos e se não são todos iguais
if len(cpf) != 11 or cpf == cpf[0] * 11:
    valido = False
else:
    # Cálculo do 1º Dígito Verificador (10º dígito)
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1
    
    # Cálculo do 2º Dígito Verificador (11º dígito)
    soma2 = 0
    for i in range(10):
        soma2 += int(cpf[i]) * (11 - i)
        
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2
    
    # Regra Final: Comparar os dígitos calculados com os informados
    valido = (int(cpf[9]) == digito1) and (int(cpf[10]) == digito2)

# Resultado
if valido:
    print(f"O CPF {entrada} é VÁLIDO.")
else:
    print(f"O CPF {entrada} é INVÁLIDO.")