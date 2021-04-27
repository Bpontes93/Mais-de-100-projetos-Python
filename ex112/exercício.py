'''
112 - Entrada de dados monetários, verificando entrada.
'''
# Dentro do pacote utilidades CeV que criamos no desafio 111, temos um módulo chamado dao.
# Crie uma função chamada leiadinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitas apenas valores que sejam monetários.

from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

n = dado.leiaDinheiro('Digite o preço: R$')
desc = dado.leiaPorcento('Qual o desconto: %')
multa = dado.leiaPorcento('Qual a multa pagando atrasado: %')

moeda.resumo(n, multa, desc)