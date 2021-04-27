# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listapar = []
listaimpar = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    elif num % 2 != 0:
        listaimpar.append(num)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
lista.sort()
listaimpar.sort()
listapar.sort()
print(f'Os números digitados foram {lista}.')
print(f'Os números pares são {listapar}.')
print(f'Os números ímpares são {listaimpar}.')
