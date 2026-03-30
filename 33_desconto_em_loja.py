'''Por ser um cliente frequente, Leonel recebeu alguns cupons de desconto para utilizar em uma loja do shopping. 
Objetivo: Desenvolver um programa que receba o valor total da compra e o valor do desconto aplicado, e calcule o valor final que Leonel deverá pagar.
Regras: O desconto é um valor fixo (em reais), não percentual.
'''


# Entrada de dados
valor_total = float(input("Digite o valor total da compra: R$ "))
valor_desconto = float(input("Digite o valor do cupom de desconto: R$ "))

# Cálculo do valor final
# Garantimos que o valor não fique negativo (mínimo R$ 0)
valor_final = max(0.0, valor_total - valor_desconto)

print("-" * 35)
if valor_desconto >= valor_total:
    print("O cupom cobriu todo o valor da compra!")
    print("Valor final a pagar: R$ 0.00")
else:
    print(f"Desconto de R$ {valor_desconto:.2f} aplicado com sucesso.")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
