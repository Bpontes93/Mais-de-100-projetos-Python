# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from operator import itemgetter
from random import randint
from time import sleep
dict = dict()
jogadores = {}

for j in range(1, 5):
    dict[f'JOGADOR {j}'] = randint(1, 6)
print('=-'*15)
for j, p in dict.items():
    print(f'O {j} fez {p} pontos')
    sleep(0.7)
ordenado = sorted(dict.items(), key=itemgetter(1), reverse=True)
r = 1

print('=-'*15)
print('{:^30}'.format('RANKING'))

for j, p in ordenado:

    print(f'{r}º Lugar: {j} com {p}.')
    r += 1
    sleep(0.7)
print('=-'*15)

'''
for j in range(1, 5):
    dado = randint(1, 6)
    print(f'O jogador {j} tirou {dado} ')
    dict['Jogador'] = j
    dict['Pontos'] = dado
    jogadores.append(dict.copy())
'''


