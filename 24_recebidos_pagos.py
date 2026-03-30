'''Sempre que Samela faz comprinhas na Shopee, ela precisa pagar um frete de R$ 20,00 se o valor da compra for inferior a R$ 100,00. Caso o valor da compra seja igual ou superior a R$ 100,00, o frete é gratuito.
Objetivo: Desenvolver um programa que receba o valor da compra feita por Samela e informe se ela precisará pagar o frete e qual o valor total da compra. Caso precise, o programa também deve mostrar quanto faltou para conseguir o frete.
Regras: Se o valor da compra for igual ou superior a R$ 100,00, Samela recebe frete grátis. Caso o valor da compra seja inferior a R$ 100,00, será cobrado um frete de R$ 20,00.
'''


# Entrada do valor da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Regra de frete
FRETE_VALOR = 20.00
META_FRETE_GRATIS = 100.00

if valor_compra >= META_FRETE_GRATIS:
    print("\nParabéns! Você ganhou FRETE GRÁTIS.")
    print(f"Total a pagar: R$ {valor_compra:.2f}")
else:
    falta = META_FRETE_GRATIS - valor_compra
    total_com_frete = valor_compra + FRETE_VALOR
    
    print(f"\nFrete de R$ {FRETE_VALOR:.2f} aplicado.")
    print(f"Faltam R$ {falta:.2f} em compras para você ganhar frete grátis!")
    print(f"Total a pagar (com frete): R$ {total_com_frete:.2f}")