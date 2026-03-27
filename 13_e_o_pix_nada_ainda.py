'''Um certo competidor com nome iniciando com P. Recebe R$ 60,20 por hora trabalhada. 
Se ele trabalhar mais que 20 horas receberá um adicional de 30%, de hora extra.
Objetivo: Desenvolva um sistema que calcule quanto este determinado competidor recebe ao fim do mês caso faça ou não horas extras no mês.
Regras: O adicional se aplica apenas sobre as horas que superem as 20h regulares de trabalho.
'''

def calcular_pagamento():
    valor_hora = 60.20
    limite_regular = 20
    adicional_extra = 1.30  # Representa os 60,20 + 30%

    horas_trabalhadas = float(input("Digite o total de horas trabalhadas no mês: "))

    if horas_trabalhadas <= limite_regular:
        # Cálculo simples sem horas extras
        pagamento_total = horas_trabalhadas * valor_hora
    else:
        # Cálculo das horas regulares (primeiras 20h)
        pagamento_regular = limite_regular * valor_hora
        
        # Cálculo das horas extras (o que excedeu 20h) com 30% de acréscimo
        horas_extras = horas_trabalhadas - limite_regular
        pagamento_extra = horas_extras * (valor_hora * adicional_extra)
        
        pagamento_total = pagamento_regular + pagamento_extra

    print(f"\nResumo do Competidor P:")
    print(f"Total de horas: {horas_trabalhadas}h")
    print(f"Valor total a receber: R$ {pagamento_total:.2f}")

calcular_pagamento()