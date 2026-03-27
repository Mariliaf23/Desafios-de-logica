'''Murilo foi passar as férias nos estados unidos, ao chegar na cidade de Boston achou a temperatura muito fria e foi olhar no termômetro de rua quantos graus estava fazendo. 
Para sua surpresa o termômetro estava em Fahrenheit.
Desenvolva um sistema que recebe a temperatura em Fahrenheit e responda a quantos graus equivale em Celsius.
Fórmula de conversão: ºC = (ºF-32)/1.8
'''

# 1. Recebe a temperatura em Fahrenheit
farenheit = float(input("Digite a temperatura em Fahrenheit (°F): "))

# 2. Aplica a fórmula de conversão
celsius = (farenheit - 32) / 1.8

# 3. Exibe o resultado formatado
print(f"A temperatura de {farenheit}°F equivale a {celsius:.1f}°C em Celsius.")
