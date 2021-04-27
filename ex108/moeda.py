# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar
# os valores como um valor monetário formatado.

'''Arquivo Moeda v2.0'''

def aumentar(vlr, t=0):
    if t != 0:
        p = t/100
        acr = vlr + (vlr * p)
    return acr


def diminuir(vlr, t=0):
    if t != 0:
        p = t/100
        desc = vlr - (vlr * p)
    return desc


def dobro(vlr):
    dobro = 2 * vlr
    return dobro


def metade(vlr):
    metade = vlr/2
    return metade


def moeda(vlr):
    vlr = f'R$ {vlr:0.2f}'
    return vlr