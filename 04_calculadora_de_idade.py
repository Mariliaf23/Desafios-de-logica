'''Desenvolva um sistema que solicite o ano de nascimento do usuário, calcule e exiba a sua idade atual'''
# definimos o ano atual (estamos em 2026)
ano_atual = 2026

# Solicitamos o ano de nascimento
# Usamos int() porque anos são números inteiros (sem vírgula)
ano_nascimento = int(input("Digite o seu ano de nascimento: "))


# Calculamos a idade
idade = ano_atual - ano_nascimento

# Exibimos o resultado
print(f"Em {ano_atual}, você tem (ou completará {idade} anos.")


