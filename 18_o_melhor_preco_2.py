'''D. Joana está no supermercado e ficou em dúvida sobre qual amaciante de roupas seria o mais barato
Objetivo: Desenvolva um sistema que receba os dois nomes e valores, dos amaciantes, informados pelo usuário e indique qual deles é o mais barato.
Regras: O sistema deve exibir claramente qual dos dois valores é o maior. Caso os valores sejam iguais, o sistema deve informar que ambos possuem o mesmo valor. Os valores podem ser inteiros ou decimais.
'''

# Entrada dos dados
nome1 = input("Nome do primeiro amaciante: ")
preco1 = float(input(f"Valor do {nome1}: R$ "))

nome2 = input("Nome do segundo amaciante: ")
preco2 = float(input(f"Valor do {nome2}: R$ "))

# Comparação
if preco1 < preco2:
    print(f"\nO {nome1} é o mais barato!")
    print(f"O maior valor é do {nome2}: R$ {preco2:.2f}")
elif preco2 < preco1:
    print(f"\nO {nome2} é o mais barato!")
    print(f"O maior valor é do {nome1}: R$ {preco1:.2f}")
else:
    print("\nAmbos possuem o mesmo valor.")