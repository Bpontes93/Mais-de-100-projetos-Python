# Crie um programa que leia, nome , sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. no final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todos as pessoas com idade acima da média.
pessoa = dict()
cadastros = list()
maisvelhos = list()
mulheres = list()
totidade = totpessoas = totmulher = 0
while True:
    pessoa['NOME'] = str(input('Digite o nome: ').capitalize())
    pessoa['SEXO'] = str(input('Digite o sexo: [F/M] ')).upper().strip()[0]
    pessoa['IDADE'] = int(input('Digite a idade: '))
    totidade += pessoa['IDADE']
    totpessoas += 1
    cadastros.append(pessoa.copy())
    if pessoa['SEXO'] == 'F':
        mulheres.append(pessoa.copy())
        totmulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar outra pessoa? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

media = totidade/2
cont = 0
for i in cadastros:
    if cadastros[cont]['IDADE'] >= media:
        maisvelhos.append(i)
        cont+=1

print('-='*30)
print(f'Foi cadastrado {totpessoas} pessoas.')
print(f'A média de idade do grupo é {media:0.1f}')
print(f'Total de {totmulher} mulheres. Sendo: ', end='')
for i in mulheres:
    print(f'{i["NOME"]}')
print(f'Os que tem idade acima da média é: ')
for i in maisvelhos:
    for k, v in i.items():
        print(f'{k}: {v}', end=' | ')