# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')).capitalize())
    temp.append(float(input('Digite o peso: Kg ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
            break
print("^~"*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menos peso foi de {men}Kg ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ', end='')
print()