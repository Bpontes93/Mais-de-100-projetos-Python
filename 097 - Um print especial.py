# Faça um programa que tenha uma função chamada escreva(), que receba qualquer parâmetro e mostre
# uma mensagem com tamanho adaptável.

def escreva(txt):
    print("-="*30)
    print("{:^60}".format(txt))
    print("-="*30)


escreva('Olá, Mundo')