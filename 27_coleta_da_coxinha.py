'''Certo dia, Emanuel teve uma ideia brilhante: convenceu os colegas de classe a realizar uma coleta para comprarem coxinhas com qualidade comprovada pela Anvisa.
Objetivo: Desenvolver um sistema que receba o valor coletado por 5 alunos e calcule a soma total da arrecadação. O sistema deve exibir o valor total coletado.
Regras: O programa deve receber 5 valores numéricos, representando o valor contribuído por cada aluno. Após somar os valores: Se o total for maior que R$ 40,00, o sistema deve exibir o valor total e a mensagem: "Emanuel sumiu!“. Caso contrário, o sistema deve mostrar apenas o valor total da coleta.
'''


total_coleta = 0

# Recebendo o valor de 5 alunos
for i in range(1, 6):
    valor = float(input(f"Valor do {i}º aluno: R$ "))
    total_coleta += valor

print("-" * 30)
print(f"Total arrecadado: R$ {total_coleta:.2f}")

# Regra do Emanuel
if total_coleta > 40.00:
    print("Emanuel sumiu!")
