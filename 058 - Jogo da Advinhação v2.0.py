# Melhore o jogo do ex. 28, onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador
# vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

num = [1, 2, 3, 4, 5]
escolhido = random.choice(num)
print('-'*45)
print('Estou pensando em um número de 0 a 10!\nSerá que você consegue acertar!')
print('-'*45)
acertou = False
palpites = 0
while not acertou:
    n = int(input('Qual o seu palpite? '))
    palpites += 1

    if n == escolhido:
       acertou = True

    else:
        if n < escolhido:
            print('Mais.. tente mais uma vez.')
        elif n > escolhido:
                print('Menos.. tente mais uma vez.')
print('Acertou! com {} tentativas. Parabéns!'.format(palpites))