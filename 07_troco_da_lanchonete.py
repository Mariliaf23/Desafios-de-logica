'''Daniel foi na padaria biju comprar um lanche. 
Desenvolva um sistema que receba o valor do lanche e o valor que Daniel pagou e por fim calcule o troco que Daniel deverá receber da padaria.
'''

# 1. Recebe o valor do lanche e o valor pago
valor_lanche = float(input("Digite o valor do lanche: R$ "))
valor_pago = float(input("Digite o valor pago por Daniel: R$ "))

# 2. Calcula a diferença (troco)
troco = valor_pago - valor_lanche

# 3. Exibe o resultado formatado
if troco >= 0:
    print(f"O troco que Daniel deverá receber é: R$ {troco:.2f}")
else:
    print(f"O valor pago é insuficiente! Faltam: R$ {abs(troco):.2f}")
    