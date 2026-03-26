'''Desenvolva um sistema que solicite o ano de nascimento do usuário, calcule e exiba a sua idade atual'''

ano_atual = 2026

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

idade = ano_atual - ano_nascimento

print(f"Em {ano_atual}, você tem (ou completará {idade} anos.")