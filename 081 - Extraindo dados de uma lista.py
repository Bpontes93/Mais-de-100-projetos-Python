# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break

lista.sort(reverse=True)
print('-='*35)
print(f'Você digitou {len(lista)} números.')
print('Sendo', end='')
for c in lista:
    print(f', {c}', end='')
print(', ', end='')
print('os números digitados de forma decrescente.')

if 5 in lista:
    print(f'O número 5 está digitado na {lista.index(5)+1}ª posição.')
else: print('Número 5 não foi digitado.')