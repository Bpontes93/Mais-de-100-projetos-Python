# Faça um programa que leia 5 válores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = [int(input('Digite um número: ')),
         int(input('Digite outro número:')),
         int(input('Digite mais um número: ')),
         int(input('Digite outro número:')),
         int(input('Digite o ultimo número:'))]

print(f'O maior número digitado foi {max(lista)} e sua posição na lista é {lista.index(max(lista))+1}.')
print(f'O menor número digitado foi {min(lista)} e sua posição na lista é {lista.index(min(lista))+1}.')

'''
lista2 = []
mai = 0
men = 0
for c in range(1,6):
    lista2.append(int(input('Digite um número para a posição{c} ')))
    if c == 0:
        mai = men = lista2[c]
    else:
        if lista2[c] > mai:
            mai = lista2[c]
        if lista2[c] < men:
            men = lista2[c]
print(f'Você digitou os valores {lista2}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v enumerate(lista2):
    if v == mai:
        print(f'{i}..., end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v enumerate(lista2):
    if v == men:
        print(f'{i}..., end='')
print()
    '''