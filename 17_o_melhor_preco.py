'''D. Joana está no supermercado e ficou em dúvida sobre qual amaciante de roupas seria o mais barato
Objetivo: Desenvolva um sistema que receba os dois valores, dos amaciantes, informados pelo usuário e indique qual deles é o mais barato.
Regras: O sistema deve exibir claramente qual dos dois valores é o mais barato. Caso os valores sejam iguais, o sistema deve informar que ambos possuem o mesmo valor. Os valores podem ser inteiros ou decimais.
'''

def comparar_amaciantes():
    print("--- Comparador de Preços: Amaciantes ---")
    
    try:
        # Entrada dos valores (podem ser inteiros ou decimais)
        valor1 = float(input("Digite o preço do primeiro amaciante (R$): "))
        valor2 = float(input("Digite o preço do segundo amaciante (R$): "))

        # Lógica de comparação
        if valor1 < valor2:
            print(f"\nO primeiro amaciante é o mais barato: R$ {valor1:.2f}")
        elif valor2 < valor1:
            print(f"\nO segundo amaciante é o mais barato: R$ {valor2:.2f}")
        else:
            print("\nAmbos os amaciantes possuem o mesmo valor.")

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos (ex: 15.90).")

comparar_amaciantes()
