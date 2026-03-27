'''O celular de José está descarregando, ele sabe que cada 1% de bateria dura cerca de 5 minutos.
Desenvolva um sistema que recebe a quantidade de bateria atual e retorna quantos minutos de vida o celular de José ainda tem.
'''

# 1. Recebe a porcentagem atual da bateria (ex: 20)
bateria = int(input("Qual a porcentagem atual da bateria do José? "))

# 2. Calcula o tempo restante (cada 1% = 5 minutos)
minutos_restantes = bateria * 5

# 3. Exibe o resultado 
print(f"\nCom {bateria}% de bateria, o celular ainda tem aproximadamente {minutos_restantes} minutos de vida.")