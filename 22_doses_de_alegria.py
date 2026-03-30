'''Sendo hoje véspera da véspera de sexta-feira, José resolveu sair para comemorar após o curso. Depois de algumas doses de alegria líquida, chegou a hora de pagar a conta.
Objetivo: Desenvolver um programa que receba o valor disponível na conta de José e o valor gasto com as doses de alegria líquida, e informe se o saldo da conta:
#Continuou positivo
#Ficou zerado 
#Ou foi para o negativo
'''

# Entrada de dados
saldo_inicial = float(input("Quanto o José tinha na conta? R$ "))
valor_gasto = float(input("Qual foi o valor total da conta? R$ "))

# Cálculo do saldo final
saldo_final = saldo_inicial - valor_gasto

# Verificação do status da conta
if saldo_final > 0:
    print(f"\nO saldo continuou POSITIVO: R$ {saldo_final:.2f}")
elif saldo_final == 0:
    print("\nO saldo ficou ZERADO. Foi na conta certa!")
else:
    print(f"\nO saldo foi para o NEGATIVO: R$ {saldo_final:.2f}")