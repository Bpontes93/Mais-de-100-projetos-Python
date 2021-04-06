# Crie um programa que leia dois valores e mostre um menu na tela. [1]Somar, [2]Multiplicar, [3]Maior,
# [4]Novos números, [5]Sair do programa. Deve realizar a operação solicitada em cada caso.

n1 = int(input('Digite um valor '))
n2 = int(input('Digite o segundo valor '))
opcao = 0

while opcao != 5:
    opcao = int(input('''ESCOLHA UMA OPÇÃO:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa'''))

    if opcao == 1:
            print('O resultado da soma é {}'.format(n1+n2))
    elif opcao == 2:
            print('0 resultado da multiplicação é {}'.format(n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
        else:
            print('o maior é {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))



print('FIM')