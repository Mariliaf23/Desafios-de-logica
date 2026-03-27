'''O supermercado Líder está embalando maçãs em caixas para transporte entre filiais. Cada caixa comporta até 12 maçãs.
Objetivo: Desenvolver um programa que receba a quantidade total de maçãs a serem embaladas e informe quantas caixas serão necessárias para concluir o empacotamento. 
Regras:Cada caixa pode conter, no máximo, 12 maçãs.Todas as maçãs devem ser embaladas, mesmo que a última caixa não fique completamente cheia.
'''

import math

# 1. Recebe a quantidade total de maçãs
total_macas = int(input("Digite a quantidade total de maçãs: "))

# 2. Calcula a quantidade de caixas (capacidade = 12)
# math.ceil garante que 13 maçãs resultem em 2 caixas, por exemplo.
caixas_necessarias = math.ceil(total_macas / 12)

# 3. Exibe a informação para o transporte
print(f"Para transportar {total_macas} maçãs, o Líder precisará de {caixas_necessarias} caixa(s).")
