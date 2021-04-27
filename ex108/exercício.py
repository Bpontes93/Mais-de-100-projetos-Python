'''
108 - Formatando Moedas em Python.
'''
#
# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar
# os valores como um valor monetário formatado.

from ex108 import moeda


n = float(input('Insira o valor: R$'))
desc = int(input('Qual o desconto pagando adiantado: %'))
multa = int(input('Qual a multa pagando atrasado: %'))
print(f'Com desconto de {desc}% é {moeda.moeda(moeda.diminuir(n, desc))}')
print(f'Com acréscimo de {multa}% é {moeda.moeda(moeda.aumentar(n, multa))}')
print(f'A metade é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro é {moeda.moeda(moeda.dobro(n))}')