'''Ane quer saber quantos passos ela anda desde a parada do ônibus até o Senac. 
Para isso ela mediu quantos passos ela caminha em um metro e quantos metros há entre a parada e o Senac.
Desenvolva um sistema que receba as informações de quantos passos Ane precisa andar para caminhar um metro, 
quantos metros ela anda e calcule quanto passos ela precisa caminhar até chegar ao Senac.
'''

# 1. Coleta os dados (usamos float para permitir números decimais)
passos_por_metro = float(input("Quantos passos a Ane dá em 1 metro? "))
distancia_metros = float(input("Qual a distância em metros da parada até o Senac? "))

# 2. Calcula o total de passos
total_passos = passos_por_metro * distancia_metros

# 3. Exibe o resultado de forma amigável
# Usamos int() no final pois não faz sentido contar "meio passo" no resultado total
print(f"\nPara percorrer {distancia_metros} metros, Ane precisará dar aproximadamente {int(total_passos)} passos.")
