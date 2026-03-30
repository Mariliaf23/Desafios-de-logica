'''Alcides está se preparando para competir no Mr. Olympia deste ano. Para isso, ele precisa calcular o seu Índice de Massa Corporal (IMC) e verificar se está dentro do padrão esperado para o evento.
Objetivo: Desenvolver um programa que receba a altura e o peso corporal de Alcides e calcule o seu IMC.
'''


# Entrada de dados
print("--- Calculadora de IMC: Rumo ao Mr. Olympia ---")
peso = float(input("Digite o peso atual (kg): ").replace(",", "."))
altura = float(input("Digite a altura (m): ").replace(",", "."))

# Cálculo do IMC
imc = peso / (altura ** 2)

print("-" * 35)
print(f"O IMC de Alcides é: {imc:.2f}")

# Classificação simples (opcional para contexto)
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade (foco em massa muscular no caso de atletas)")
