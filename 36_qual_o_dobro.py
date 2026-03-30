'''Desafio: desenvolva um sistema que receba um número e informe qual o dobro do seu valor
Regra: O sistema deve calcular o valor do dobro do número recebido.
Complicando: Faça o sistema questionar quantas vezes o usuário quer que dobre o número e mostre todos os valores calculados.
'''


# Entrada inicial
numero = float(input("Digite o número inicial: ").replace(",", "."))
vezes = int(input("Quantas vezes você deseja dobrar esse número? "))

print(f"\nDobrando o valor {vezes} vezes:")
print("-" * 30)

# Loop para calcular e mostrar as progressões
valor_atual = numero
for i in range(1, vezes + 1):
    valor_atual = valor_atual * 2
    print(f"{i}ª dobra: {valor_atual}")

print("-" * 30)
print(f"Resultado final: {valor_atual}")
