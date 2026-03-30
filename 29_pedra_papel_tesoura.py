'''Desafio: desenvolva um sistema que receba dois valores (pedra, papel ou tesoura) e indique quem ganhou o jogo.
Regra: Pedra ganha de tesoura e perde de papel, papel ganha de pedra e perde de tesoura, tesoura perde de pedra e ganha de papel.
Complicando: O sistema deve receber a escolha do usuário e sortear um valor para ele mesmo. Após isso o sistema deve informar quem ganhou o jogo.
Melhor de três: Faça o jogo se repetir por 3 vezes, quem tiver ganho mais vezes é o grande campeão
'''


import random

opcoes = ["pedra", "papel", "tesoura"]
vitorias_usuario = 0
vitorias_computador = 0

print("--- Jogo: Melhor de Três ---")

for rodada in range(1, 4):
    print(f"\nRODADA {rodada}")
    usuario = input("Escolha Pedra, Papel ou Tesoura: ").lower()
    
    # Sorteio do computador
    computador = random.choice(opcoes)
    print(f"O computador escolheu: {computador}")

    # Lógica do jogo
    if usuario == computador:
        print("Empate nesta rodada!")
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "papel" and computador == "pedra") or \
         (usuario == "tesoura" and computador == "papel"):
        print("Você venceu esta rodada!")
        vitorias_usuario += 1
    else:
        print("O computador venceu esta rodada!")
        vitorias_computador += 1

# Resultado Final 
print("\n" + "="*20)
print(f"Placar Final: Você {vitorias_usuario} x {vitorias_computador} Computador")

if vitorias_usuario > vitorias_computador:
    print("Você é o GRANDE CAMPEÃO!")
elif vitorias_computador > vitorias_usuario:
    print("O Computador é o GRANDE CAMPEÃO!")
else:
    print("O jogo terminou em EMPATE GERAL!")
