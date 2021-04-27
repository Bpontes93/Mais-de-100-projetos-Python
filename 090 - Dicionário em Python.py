# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dic = dict()
dic['NOME'] = str(input('Nome: ').capitalize())
dic['MÉDIA'] = int(input(f'Média do {dic["NOME"]}: '))
if dic['MÉDIA'] >= 5:
    dic['SITUAÇÃO'] = 'Aprovado'
else: dic['SITUAÇÃO'] = 'REPROVADO'
print('=-'*30)
""" 1ª Forma de apresentação para o usuário"""

for k, v in dic.items():
    print(f'{k}: {v}')



