# Reescreva a função leiaInt() feita no desafio 104. incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com
# a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um \033[1;38mNÚMERO INTEIRO\033[m\033[1;31m válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31;mEntrada de dados interrompida pelo usuário.\033[1;m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um \033[1;38mNÚMERO REAL\033[m\033[1;31m válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31;mEntrada de dados interrompida pelo usuário.\033[1;m')
            return 0
        else:
            return n


n = leiaInt('Digite um Número Inteiro: ')
f = leiaFloat('Digite um Número Real: ')
print(f'\033[1;34mVocê acabou de digitar o número Inteiro {n}\033[m')
print(f'\033[1;34mVocê acabou de digitar o número Real {f}\033[m')