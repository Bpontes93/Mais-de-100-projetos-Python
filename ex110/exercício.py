'''
110 - Reduzindo o Programa.
'''
# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado
# até aqui.

from ex110 import moeda
n = float(input('Insira o valor: R$'))
desc = int(input('Qual o desconto pagando adiantado: %'))
multa = int(input('Qual a multa pagando atrasado: %'))

moeda.resumo(n, multa, desc)