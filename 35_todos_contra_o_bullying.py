'''Após descobrir quem fez bullying contra um de nossos companheiros alguns alunos se juntaram para ter uma conversa gentil e amigável com o agressor, fora das dependências e responsabilidades do Senac. Para evitar covardias decidiram que apenas o maior do grupo iria dialogar com o agressor.
Desenvolva um sistema que receba a altura, de um número indeterminado de alunos, e defina qual deles é o maior e qual é o menor. O sistema deve dizer quantas pessoas foram cadastradas.
'''


alturas = []

print("--- Cadastro de Participantes (Diálogo Amigável) ---")
print("Digite '0' para encerrar o cadastro e ver o resultado.\n")

while True:
    entrada = input("Digite a altura do aluno (ex: 1.85): ").replace(",", ".")
    altura = float(entrada)

    if altura == 0:
        break
    
    alturas.append(altura)

# Verificação se houve algum cadastro antes de exibir o resultado
if len(alturas) > 0:
    maior_altura = max(alturas)
    menor_altura = min(alturas)
    total_pessoas = len(alturas)

    print("-" * 40)
    print(f"Total de pessoas no grupo: {total_pessoas}")
    print(f"O maior aluno (quem irá dialogar) tem: {maior_altura:.2f}m")
    print(f"O menor aluno do grupo tem: {menor_altura:.2f}m")
else:
    print("\nNenhum aluno foi cadastrado.")
