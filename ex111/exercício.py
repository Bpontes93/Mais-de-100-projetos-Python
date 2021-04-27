'''
111 - Transformando módulos em Pacotes.
'''
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
# mantenha tudo funcionando.
from ex111.utilidadesCeV import moeda

n = float(input('Insira o valor: R$'))
desc = int(input('Qual o desconto pagando adiantado: %'))
multa = int(input('Qual a multa pagando atrasado: %'))

moeda.resumo(n, multa, desc)
