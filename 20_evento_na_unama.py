'''Fernando está organizando um evento de “Programação em Python” na Unama. No entanto, esse evento é restrito a pessoas que já atingiram a maioridade.
Objetivo: Desenvolver um programa que receba a idade de um participante e informe se ele é maior de idade.
Regra: Considera-se maior de idade quem tem 18 anos ou mais.
'''


# Entrada da idade
idade = int(input("Informe a idade do participante: "))

# Verificação da maioridade
if idade >= 18:
    print("O participante é maior de idade. Acesso permitido ao evento!")
else:
    print("O participante é menor de idade. Acesso restrito.")