'''Desenvolva um sistema que solicite três números inteiros, calcule e exiba a média dentre estes números.'''

# Solicita os três números inteiros ao usuário
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Realiza o cálculo da média
# A soma deve estar entre parênteses para ser feita antes da divisão
media = (n1 + n2 + n3) / 3

# Exibe o resultado final
print(f"A média dos números {n1}, {n2} e {n3} é: {media}")