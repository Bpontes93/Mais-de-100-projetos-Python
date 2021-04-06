# Faça o GAME: Pedra, Papel, Tesoura.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=-'*11)
print ('Computador jogou {}'.format(itens[computador]))
print('JOgador jogou {}'.format(itens[jogador]))
print('\33[1;31;m=-\33[m'*11)

if computador == 0:
	if jogador == 0:
            print('EMPATE')
	elif jogador == 1:
            print('JOGADOR VENCE')
	elif jogador == 2:
            print('COMPUTADOR VENCE')
	else:
	        print('JOGADA INVÁLIDA!')

elif computador == 1:
	if jogador == 0:
	    print('COMPUTADOR VENCE')
	elif jogador == 1:
	    print('EMPATE')
	elif jogador == 2:
	    print('JOGADOR VENCE')
	else:
	    print('JOGADA INVÁLIDA!')


elif computador == 2:
	if jogador == 0:
	    print('JOGADOR VENCE')
	elif jogador == 1:
	    print('COMPUTADOR VENCE')
	elif jogador == 2:
	    print('EMPATE')
	else:
	    print('JOGADA INVÁLIDA!')


print('\33[1;31;m=-\33[m'*11)