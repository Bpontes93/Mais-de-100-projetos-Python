# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
# pares e ímpares em ordem crescente.

lista = [[],[]]

for n in range (1,8):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
lista.sort()

print('-~'*30)
print(f'Os pares são {lista[0]}')
print(f'Os ímpares são {lista[1]}')




