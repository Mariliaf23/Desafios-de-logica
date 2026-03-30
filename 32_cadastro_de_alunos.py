'''O Senac precisa cadastrar o pagamento da mensalidade dos alunos inscritos em determinado curso.
Objetivo: Desenvolver um sistema que receba os valores das mensalidades pagas pelos alunos, até que o usuário informe que os pagamentos acabaram. Ao final, o sistema deve exibir o total pago em mensalidades.
Regras: O sistema deve permitir a entrada de múltiplos valores (representando mensalidades pagas), um por vez. A entrada de valores deve continuar até o usuário indicar que não há mais pagamentos. Ao final, o programa deve somar todos os valores informados e exibir o total pago.
'''


total_pago = 0.0

print("--- Sistema de Mensalidades Senac ---")
print("(Digite '0' para encerrar e ver o total)")

while True:
    # Recebe o valor da mensalidade
    entrada = input("Valor da mensalidade paga: R$ ").replace(",", ".")
    valor = float(entrada)

    # Condição de parada (se o valor for 0, encerra o loop)
    if valor == 0:
        break
    
    # Soma o valor ao total acumulado
    total_pago += valor

print("-" * 35)
print(f"Total arrecadado em mensalidades: R$ {total_pago:.2f}")
print("Sistema finalizado.")
