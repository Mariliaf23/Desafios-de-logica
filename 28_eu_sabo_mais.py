'''Augusto e Adriano estavam realizando alguns cálculos para resolver uma atividade em sala, porém eles alcançaram resultados diferentes.
Objetivo: Desenvolver um sistema que os ajude a resolver o impasse. O sistema deve receber um número e imprimir a tabuada desse número de 1 a 10.
Regras: O programa deve solicitar um número inteiro. Em seguida, deve exibir a tabuada desse número, multiplicando-o de 1 a 10. Cada linha deve mostrar a operação no formato: número x multiplicador = resultado
'''


# Solicita o número para o cálculo
numero = int(input("Digite o número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
print("-" * 15)

# Gera a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("-" * 15)