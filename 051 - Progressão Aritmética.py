# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

termo = int(input(' Insira o PRIMEIRO TERMO: '))
razao = int(input('Insira a RAZÃO: '))
dec = termo + (10 - 1) * razao
for c in range (termo, dec + razao, razao):
    print('{}'.format(c), end='-> ')
print('ACABOU !')