# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
# e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

'''Arquivo Moeda v1.0'''


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
