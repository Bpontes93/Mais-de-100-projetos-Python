# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela mensagem de acordo.

n1 = int(input('Insira um valor: '))
n2 = int(input('Insira o segundo valor: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n1 < n2:
    print('O SEGUNDO valor é maior')

elif n1 == n2:
    print('Os valores são IGUAIS')