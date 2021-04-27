# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além de idade, com quantos anos a pessoa vai se
# aposentar.

from datetime import datetime
cadastros = list()
pessoa = dict()
ano = datetime.today().year
while True:
    pessoa['NOME'] = str(input('NOME: ').capitalize())
    pessoa['ANO DE NASCIMENTO'] = int(input('ANO DE NASCIMENTO: '))
    pessoa['IDADE'] = ano - pessoa['ANO DE NASCIMENTO']
    pessoa['CTPS'] = int(input('Nº DE CTPS: [0 se não tiver] '))
    if pessoa['CTPS'] != 0:
        pessoa['ANO DE CONTRATAÇÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
        pessoa['SALÁRIO'] = int(input('SALÁRIO: '))
        break
    else:
        break
print(pessoa)
for k, v in pessoa.items():
    print(f'{k}: {v}.')

if pessoa['CTPS'] != 0:
    idadecontratado = pessoa['ANO DE CONTRATAÇÃO'] - pessoa['ANO DE NASCIMENTO']
    idadeaposentadoria = idadecontratado + 60
    print(f'Irá se aposentar com {idadeaposentadoria} anos.')