'''Desenvolva um sistema que solicite dois números ao usuário.
Objetivo: O sistema deve perguntar ao usuário qual das cinco operações aritméticas (soma, subtração, divisão, multiplicação e exponenciação) deseja realizar com os dois números e exibir os resultados.
Regra: Use funções para realizar as operações
'''

def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Erro: Divisão por zero"
def exponenciar(a, b): return a ** b

def calculadora():
    print("--- Sistema Aritmético ---")
    
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        
        print("\nEscolha a operação:")
        print("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Exponenciação")
        opcao = input("Digite o número da opção (1-5): ")

        if opcao == '1':
            print(f"Resultado: {somar(n1, n2)}")
        elif opcao == '2':
            print(f"Resultado: {subtrair(n1, n2)}")
        elif opcao == '3':
            print(f"Resultado: {multiplicar(n1, n2)}")
        elif opcao == '4':
            print(f"Resultado: {dividir(n1, n2)}")
        elif opcao == '5':
            print(f"Resultado: {exponenciar(n1, n2)}")
        else:
            print("Opção inválida.")

    except ValueError:
        print("Erro: Por favor, insira apenas valores numéricos.")

calculadora()
