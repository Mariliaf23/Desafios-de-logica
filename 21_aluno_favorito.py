'''Ewerton e Rodrigo estão discutindo sobre quem foi o aluno favorito do professor João. Como não conseguem chegar a um acordo, decidem resolver a disputa no “par ou ímpar”.
Objetivo: Desenvolver um programa que receba um número e informe se ele é par ou ímpar.
Regra: Um número é par quando é divisível por 2. Caso contrário, ele é ímpar. O sistema deve continuar a realizar verificações de par ou ímpar até que o usuário interrompa sua execução.
'''


while True:
    # Entrada do número
    num_str = input("\nDigite um número (ou 'sair' para encerrar): ")

    # Condição de parada
    if num_str.lower() == 'sair':
        print("Disputa encerrada!")
        break

    # Conversão e verificação
    numero = int(num_str)

    if numero % 2 == 0:
        print(f"O número {numero} é PAR!")
    else:
        print(f"O número {numero} é ÍMPAR!")