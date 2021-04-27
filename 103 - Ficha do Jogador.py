# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. o programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
    '''
    
    :param jogador: Nome do Atleta. 
    :param gols: Quantidade de gols marcados.
    :return: 
    '''
    print(f'O jogador {jog} fez {gol} gols no campeonato')
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
