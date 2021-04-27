# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date


def voto(idade):
    '''
    fun voto: retorna a situação de voto de acordo com idade analisada .
    :param idade: idade em anos.
    :return: Situação do voto.
    '''
    if idade >= 60 or idade < 18:
        return 'VOTO OPCIONAL'
    elif idade > 18 and idade < 60:
        return 'VOTO OBRIGÁTORIO'
    elif idade < 16:
        return 'VOTO NEGADO'

idade = date.today().year - (int(input('Em qual ano você nasceu? ')))
print(f'Sua Idade é {idade}, sendo: ', end='')
print(voto(idade))
