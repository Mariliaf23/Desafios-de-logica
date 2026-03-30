'''Desafio: Desenvolva um sistema de calculadora que realize as quatro operações (adição, subtração, multiplicação e divisão) com um números indefinido de elementos.
Regra: O sistema deve ser capaz de realizar várias operações sequenciais, até que o usuário decida parar o sistema.
O usuário deve:
# Inserir um número
# Indicar qual operação deseja realizar
# Inserir outro número
# Receber o resultado
# Indicar se deseja continuar a conta
'''


# Inicialização
resultado = float(input("Digite o primeiro número: "))

while True:
    print("\nOperações: [+] Somar | [-] Subtrair | [*] Multiplicar | [/] Dividir")
    operacao = input("Qual operação deseja realizar? ")
    
    proximo_numero = float(input("Digite o próximo número: "))

    # Processamento da operação
    if operacao == '+':
        resultado += proximo_numero
    elif operacao == '-':
        resultado -= proximo_numero
    elif operacao == '*':
        resultado *= proximo_numero
    elif operacao == '/':
        if proximo_numero != 0:
            resultado /= proximo_numero
        else:
            print("Erro: Divisão por zero não permitida!")
            continue
    else:
        print("Operação inválida!")
        continue

    print(f"\nResultado atual: {resultado}")

    # Condição de continuidade
    continuar = input("Deseja continuar a conta? (s/n): ").lower()
    if continuar != 's':
        break

print(f"\nCalculadora encerrada. Resultado final: {resultado}")
