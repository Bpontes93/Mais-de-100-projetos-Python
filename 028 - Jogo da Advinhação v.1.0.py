#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
#peça ao usuário tentar descobrir qual foi o número escolhido pelo
import random

num = [1, 2, 3, 4, 5]
escolhido = random.choice(num)
print('-'*45)
n = int(input('Tente advinhar o número que estou pensando!\nDigite seu palpite: '))
print('-'*45)
if n == escolhido:
    print('Parabéns você acertou!')

else:
    print('Ops! Não foi dessa vez! Eu pensei no número {}!'.format(escolhido))
