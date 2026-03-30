'''D. Joana está no supermercado e ficou em dúvida sobre qual amaciante de roupas seria o mais barato
Objetivo: Desenvolva um sistema que receba os dois nomes e valores e volume, dos amaciantes, informados pelo usuário e indique qual deles é o mais barato.
Regras: O sistema deve exibir claramente qual dos dois valores é o maior. Caso os valores sejam iguais, o sistema deve informar que ambos possuem o mesmo valor. Os valores podem ser inteiros ou decimais.
'''

# Entrada do Amaciante 1
nome1 = input("Nome do 1º amaciante: ")
preco1 = float(input(f"Valor do {nome1}: R$ "))
vol1 = float(input(f"Volume do {nome1}: "))

# Entrada do Amaciante 2
nome2 = input("Nome do 2º amaciante: ")
preco2 = float(input(f"Valor do {nome2}: R$ "))
vol2 = float(input(f"Volume do {nome2}: "))

# Cálculo do preço por unidade (para comparação justa)
custo1 = preco1 / vol1
custo2 = preco2 / vol2

print("-" * 30)

if custo1 < custo2:
    print(f"O {nome1} é o mais barato!")
    print(f"O maior valor proporcional é o do {nome2}: R$ {custo2:.2f} por unidade.")
elif custo2 < custo1:
    print(f"O {nome2} é o mais barato!")
    print(f"O maior valor proporcional é o do {nome1}: R$ {custo1:.2f} por unidade.")
else:
    print("Ambos possuem o mesmo valor proporcional.")