'''Crie um sistema de cadastro de usuário que registre as informações de “nome, sexo, endereço, cidade, estado, CEP, telefone, data de nascimento, RG, nome do pai, nome da mãe e grau de escolaridade” do usuário.

O sistema deve exibir as informações do usuário em um texto amigável.
'''

print("--- SISTEMA DE CADASTRO DE USUÁRIO ---")
print("Por favor, preencha as informações abaixo:\n")

# Coleta de dados
nome = input("Nome completo: ")
sexo = input("Sexo: ")
endereco = input("Endereço: ")
cidade = input("Cidade: ")
estado = input("Estado: ")
cep = input("CEP: ")
telefone = input("Telefone: ")
nascimento = input("Data de Nascimento: ")
rg = input("RG: ")
pai = input("Nome do pai: ")
mae = input("Nome da mãe: ")
escolaridade = input("Grau de escolaridade: ")

# Exibição das informações em um texto amigável
print("\n" + "="*40)
print("     CADASTRO REALIZADO COM SUCESSO")
print("="*40)

texto_amigavel = f"""
Olá, {nome}! É um prazer ter você em nosso sistema.

Aqui está o resumo dos seus dados para conferência:
--------------------------------------------------
LOCALIZAÇÃO E CONTATO:
Residente em {endereco}, na cidade de {cidade}/{estado} (CEP: {cep}).
Seu telefone de contato é {telefone}.

DOCUMENTAÇÃO E PESSOAL:
Registrado(a) com o RG {rg}, nascido(a) em {nascimento}.
Sexo: {sexo}.
Grau de escolaridade atual: {escolaridade}.

FILIAÇÃO:
Filho(a) de {mae} e {pai}.
--------------------------------------------------
Os dados acima foram salvos corretamente em nossa base.
"""

print(texto_amigavel)