'''Desafio: Desenvolva um sistema que receba três número diferentes e indique qual o maior deles.
Regra: O sistema deve calcular qual o maior número dentre os recebidos.
Complicando: Após calcular qual o maior número o sistema deve receber mais dois números para definir qual o maior entre os três, até que o usuário interrompa o sistema.
'''


print("--- Comparador de Números ---")

# Passo 1: Recebe os três primeiros números
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))

# Define o maior inicial
maior = max(n1, n2, n3)
print(f"\nO maior número entre os três é: {maior}")

# Passo 2: Loop para adicionar mais dois números por vez
while True:
    continuar = input("\nDeseja comparar com mais dois números? (s/n): ").lower()
    if continuar != 's':
        break
    
    n4 = float(input("Digite o próximo número: "))
    n5 = float(input("Digite outro número: "))
    
    # Compara o antigo "maior" com os dois novos
    maior = max(maior, n4, n5)
    
    print(f"O novo maior número entre todos os informados é: {maior}")

print(f"\nSistema encerrado. O maior número final foi: {maior}")
