'''Desafio: desenvolva um sistema que sorteie um número entre 1 e 10 e receba um número do usuário. O sistema deve comparar os dois números e informar se o usuário acertou o número sorteado.
Regra: use a biblioteca útil para sortear o número.
Complicando: Faça o sistema informar se o número que o usuário informou é maior ou menor que o número sorteado. O sistema deve indicar quantas tentativas foram necessárias para acertar o número.
'''


import random

# Sorteio do número entre 1 e 10
numero_sorteado = random.randint(1, 10)
tentativas = 0
acertou = False

print("--- Jogo da Adivinhação ---")
print("Tente adivinhar o número que eu sorteei entre 1 e 10!")

while not acertou:
    palpite = int(input("\nQual o seu palpite? "))
    tentativas += 1
    
    if palpite == numero_sorteado:
        print(f"Parabéns! Você acertou o número {numero_sorteado}.")
        print(f"Total de tentativas: {tentativas}")
        acertou = True
    elif palpite < numero_sorteado:
        print("Errou! O número sorteado é MAIOR que o seu palpite.")
    else:
        print("Errou! O número sorteado é MENOR que o seu palpite.")

print("Fim de jogo!")
