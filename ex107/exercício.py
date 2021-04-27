'''
107 - Módulos em Python.
'''
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
# e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from ex107 import moeda

n = float(input('Insira o valor: R$'))
desc = int(input('Qual o desconto pagando adiantado: %'))
multa = int(input('Qual a multa pagando atrasado: %'))
print(f'Com desconto de {desc}% é {moeda.diminuir(n, desc)}')
print(f'Com acréscimo de {multa}% é {moeda.aumentar(n, multa)}')
print(f'A metade é {moeda.metade(n)}')
print(f'O dobro é {moeda.dobro(n)}')

