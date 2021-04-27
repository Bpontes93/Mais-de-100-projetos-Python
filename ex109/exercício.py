'''
109 - Formatando Moedas em Python v2.
'''
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando por elas vai sei ou não formatado pela função moeda(), desenvolvida no desafio 108.

from ex109 import moeda

n = float(input('Insira o valor: R$'))
desc = int(input('Qual o desconto pagando adiantado: %'))
multa = int(input('Qual a multa pagando atrasado: %'))
print(f'Com desconto de {desc}% é {moeda.diminuir(n, desc, True)}')
print(f'Com acréscimo de {multa}% é {moeda.aumentar(n, multa, True)}')
print(f'A metade é {moeda.metade(n, True)}')
print(f'O dobro é {moeda.dobro(n, True)}')
