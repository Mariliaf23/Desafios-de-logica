'''Na marinha, Emanuel era responsável por acompanhar o desempenho dos militares durante os treinamentos de natação. 
Para isso, ele precisava registrar o tempo de cada marinheiro e avaliar se o resultado foi satisfatório.
Objetivo: Desenvolver um programa que receba a graduação de um militar e o tempo (em segundos) que ele levou para concluir uma prova de natação. 
O sistema deve verificar se a graduação é válida e, em seguida, avaliar o desempenho do militar com base no tempo informado.
Regras: Validação de graduação: O sistema deve aceitar apenas as graduações válidas da Marinha do Brasil. 
Avaliação do tempo de prova: Se o tempo for maior que 40 segundos, o desempenho é considerado muito ruim. 
Se o tempo estiver entre 30 e 40 segundos (inclusive), o desempenho está bom, mas pode melhorar. Se o tempo for menor que 30 segundos, o desempenho é excelente.
'''

def avaliar_desempenho_marinha():
    # Lista simplificada de graduações válidas (Praças)
    graduacoes_validas = [
        "MARINHEIRO", "CABO", "TERCEIRO-SARGENTO", 
        "SEGUNDO-SARGENTO", "PRIMEIRO-SARGENTO", "SUBOFICIAL"
    ]

    print("--- Sistema de Avaliação de Natação (Marinha) ---")
    graduacao = input("Digite a graduação do militar: ").strip().upper()

    # Validação da Graduação
    if graduacao not in graduacoes_validas:
        print(f"Erro: '{graduacao}' não é uma graduação válida para este registro.")
        return

    try:
        tempo = float(input("Digite o tempo da prova (em segundos): "))

        # Avaliação do Tempo
        if tempo < 30:
            resultado = "Excelente"
        elif 30 <= tempo <= 40:
            resultado = "Bom, mas pode melhorar"
        else:
            resultado = "Muito ruim"

        print(f"\nRelatório Final:")
        print(f"Militar: {graduacao}")
        print(f"Tempo: {tempo}s")
        print(f"Desempenho: {resultado}")

    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido para o tempo.")

avaliar_desempenho_marinha()