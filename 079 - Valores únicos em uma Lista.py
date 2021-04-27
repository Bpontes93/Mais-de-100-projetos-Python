# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.
lista = []
while True:
        num = [int(input('Digite um número: '))]
        if num in lista:
            print('Número repetido, não adicionado! ')
        else:
            lista.append(num)
        resp = ' '
        while resp not in "SN":
            resp = str(input('Deseja continuar? S/N')).upper().strip()[0]
        if resp == 'N':
             break
lista.sort()
for c in lista:
    print(f'{c}...', end='')
print(f'Você digitou {len(lista)} números distintos no total.')


'''
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
números.sort()
print(f'Você digitou os valores {números}')

'''