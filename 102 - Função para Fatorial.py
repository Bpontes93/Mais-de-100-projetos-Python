# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo fatorial.
from time import sleep


def fatorial(num=1, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor Fatorial de um número num.
    '''

    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == True:
        for c in range(num, 0, -1):
            if c > 1:
                print(f'{c} x ', end='', flush=True)
                sleep(0.3)
            else:
                print(f'{c} = ', end='', flush=True)
                sleep(0.3)
    return f



print(fatorial(5, True))