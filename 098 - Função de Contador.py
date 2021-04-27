# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio,
# fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função
# criada:
# A) de 1 até 10, de 1 em 1.
# B) de 10 até 0, de 2 em 2.
# C) Uma contagem personalizada.

from time import sleep


def contador(i, f, p):
    print('Iniciando a CONTAGEM...')
    print(f'Inicio: {i} / Fim: {f} / Passo: {p}')
    for n in range(i, f+1, p):

        print(f"{n}.. ", end='', flush=True)
        sleep(0.4)
    print(' FIM ')
    print()

contador(1, 10, 1)
contador(10, 0, -2)
print('AGORA É SUA VEZ>>>')
contador(int(input('Digite o Inicio: ')),
         int(input('Digite o Fim: ')),
         int(input('Digite o passo: ')))


