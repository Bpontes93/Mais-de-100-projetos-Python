# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar().
# A primeira função vai sortear 5 números e vai colocár-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep
números = list()

def sorteia(lista):
    print("Sorteando os números... ")
    for c in range(0, 5):
        n = randint(0, 50)
        números.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print()
    print('-'*60)
def somapar(lista):
    s = 0
    print('Os números pares são: ')
    for i in lista:
        if i % 2 ==0:
            s += i
            print(f'{i}... ', end='', flush=True)
            sleep(0.3)
    print()
    sleep(0.3)
    print(f'A soma dos pares é \033[1;32;m{s}\33[m')


sorteia(números)
somapar(números)
