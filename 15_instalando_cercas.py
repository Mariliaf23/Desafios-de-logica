'''Rayan comprou um novo terreno e precisa cercá-lo para demarcar sua propriedade. 
Sabe-se que o terreno tem formato retangular perfeito (ou seja, lados opostos iguais e ângulos retos).
Objetivo: Desenvolver um programa que receba os comprimentos dos dois lados do terreno e calcule quantos metros de cerca serão necessários para cercar toda a área.
Regras: O terreno é um retângulo. A quantidade de cerca necessária corresponde ao perímetro do retângulo.
'''

def calcular_cerca():
    print("--- Cálculo de Cercamento de Terreno ---")
    
    try:
        lado_a = float(input("Digite o comprimento do primeiro lado (metros): "))
        lado_b = float(input("Digite o comprimento do segundo lado (metros): "))

        # Regra do Perímetro: P = 2 * (base + altura)
        perimetro = 2 * (lado_a + lado_b)

        print(f"\nResultado para o terreno de Rayan:")
        print(f"Dimensões: {lado_a}m x {lado_b}m")
        print(f"Total de cerca necessária: {perimetro:.2f} metros lineares.")

    except ValueError:
        print("Erro: Insira apenas números para as medidas dos lados.")

calcular_cerca()
