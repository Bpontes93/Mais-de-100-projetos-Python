# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função
# input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.


def leiaInt(msg):
    '''
    - Validação de dados (Int)
    :param msg: recebe o caracter de entrada 
    :return: se o carracter for int, volta como return.
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um Número: ')
print(f'\033[1;34mVocê acabou de digitar o número {n}\033[m')