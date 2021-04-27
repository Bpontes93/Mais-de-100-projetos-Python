# Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
cadastros = list()
jogador = dict()
while True:
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
    cadastros.append(jogador.copy())
    resp = " "
    while resp not in 'SN':
        resp = str(input("Deseja continuar: [S/N]")).upper().strip()[0]
    if resp == "N":
        break
print(f'Os jogadores cadastrados foi: ')

for i in cadastros:
    print('=-' * 30)
    for k, v in i.items():

        print(f"{k}: {v}")
