# Dentro do pacote utilidades CeV que criamos no desafio 111, temos um módulo chamado dao.
#  Crie uma função chamada leiadinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitas apenas valores que sejam monetários.



'''Arquivo Moeda v5.0'''


def aumentar(vlr, t=0, format=False):
    if t != 0:
        p = t/100
        acr = vlr + (vlr * p)
    if format:
        acr = f'R${acr:0.2f}'
    return acr


def diminuir(vlr, t=0, format=False):
    if t != 0:
        p = t/100
        desc = vlr - (vlr * p)
    if format:
        desc = f'R${desc:0.2f}'
    return desc


def dobro(vlr, format=False):
    dobro = 2 * vlr
    if format:
        dobro = f'R${dobro:0.2f}'
    return dobro


def metade(vlr, format=False):
    metade = vlr/2
    if format:
        metade = f'R${metade:0.2f}'
    return metade


def resumo(vlr, acr, desc):
    lista = {
        'Preço analisado': vlr,
        'Dobro do preço': dobro(vlr),
        'Metade do preço': metade(vlr),
        f'{acr}%, de aumento': aumentar(vlr, acr),
        f'{desc}%, de redução': diminuir(vlr, desc)
    }
    print('-'*30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-'*30)
    for k, v in lista.items():
        print(f'{k:15}', end=' ')
        print('{:>14}'.format(f'R${v:0.2f}'))

    print('-'*30)
