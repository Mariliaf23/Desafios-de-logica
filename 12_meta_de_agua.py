'''O nutricionista de Lucas informou que a quantidade diária de água recomendada é de 15 ml por quilo de peso corporal. 
Lucas utiliza um copo de 250 ml para se hidratar.
Objetivo: Desenvolver um programa que receba o peso corporal de Lucas e calcule quantos copos de água ele deve tomar por dia para atingir a meta recomendada.
Regras: A recomendação é de 15 ml de água por quilo de peso. Cada copo utilizado por Lucas tem capacidade para 250 ml. 
O resultado deve indicar quantos copos inteiros são necessários para atingir a meta.
'''

import math

# 1. ENTRADA: Recebe o peso de Lucas
peso = float(input("Digite o peso corporal de Lucas (kg): "))

# 2. PROCESSAMENTO: 
# Primeiro calculamos a meta total em ml
meta_diaria_ml = peso * 15

# Depois calculamos quantos copos de 250ml cabem nessa meta
# Usamos math.ceil para garantir que a meta seja atingida
total_copos = math.ceil(meta_diaria_ml / 250)

# 3. SAÍDA: Exibe o resultado amigável
print(f"\nPara o peso de {peso}kg, a meta diária é de {meta_diaria_ml}ml.")
print(f"Lucas deve tomar {total_copos} copos de 250ml para atingir essa meta.")