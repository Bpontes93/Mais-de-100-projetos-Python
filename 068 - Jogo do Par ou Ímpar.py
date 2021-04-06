# Faça um programa que jogue par ou ímpar com o cumputador. O jogo só será interrompido quando o
# jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vt = 0
while True:
    npc = randint(0, 10)
    nj = int(input('Insira seu número: '))
    aposta = str(input('PAR ou ÍMPAR? [P/I] ')).upper().strip()[0]

    n = nj + npc
    print(f'O computador escolheu {npc}, você escolheu {nj}, soma {npc+nj}')
    if aposta in'Pp':
        if n % 2 == 0:
            print('Boa, é PAR\nVocê venceu')
            vt += 1
        else:
            print('É ÍMPAR!\nVocê Perdeu!')
            break
    if aposta in 'Ii':
        if n % 2 == 0:
            print('É PAR!\nVocê perdeu!')
            break
        else:
            print('Boa, é ÍMPAR\nVocê venceu!')
            vt += 1

print(f'Você venceu {vt} vezes! ')