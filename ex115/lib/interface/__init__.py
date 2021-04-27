from ex115.lib.cores import *
from time import sleep


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            cabeçalho(vermelho('Erro! Digite um número inteiro válido!'))
            sleep(0.3)
            continue
        except (KeyboardInterrupt):
            cabeçalho(vermelho('Entrada de dados interrompida pelo usuário.'))
            return 0
        else:
            return n


def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista, cor=0):
    cabeçalho(amarelo('MENU PRINCIPAL'))
    c = 1
    for item in lista:
        print(f'{amarelo(c)} - {azul(item)}')
        c += 1
    print(linha())
    opc = leiaInt(amarelo('Sua Opção: '))
    return opc


def abrirMenu(msg):
    while True:
        try:
            n = str(input(msg)).upper().strip()[0]
        except (ValueError, TypeError):
            cabeçalho(vermelho('Erro! Digite uma resposta válida!'))
            sleep(0.3)
            continue
        except (KeyboardInterrupt):
            cabeçalho(vermelho('Entrada de dados interrompida pelo usuário.'))

        return n

def fechaPrograma(a=False):
    if a == True:
        print('-' * 42)
        print(vermelho('Saindo do sistema'), end='')
        x = ['.'] * 3
        for i in x:
            print(vermelho(i), end='', flush=True)
            sleep(0.4)
        print(vermelho(' Até Logo!'))
        print('-' * 42)
        sleep(0.7)


