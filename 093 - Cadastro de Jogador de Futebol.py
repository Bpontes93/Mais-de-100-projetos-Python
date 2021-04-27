# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
# partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.

jogador = dict()
totgol = 0
jogador['NOME'] = str(input('Nome do Atleta: ').capitalize())
jogador['PARTIDAS'] = int(input('Total de partidas: '))

for v in range(jogador['PARTIDAS']):
    gol = int(input(f'Marcou quantos gols na {v+1}ª partida? '))
    totgol += gol
jogador['GOLS MARCADOS'] = totgol
jogador['MÉDIA DE GOLS POR PARTIDA'] = jogador['GOLS MARCADOS'] / jogador['PARTIDAS']
print('-='*15)
print('{:^30}'.format("FICHA DO ATLETA"))
print('=-'*15)
for k, v in jogador.items():
    if v == jogador['MÉDIA DE GOLS POR PARTIDA']:
        print(f'{k}: {v:0.2f}')
    else:
        print(f'{k}: {v}')