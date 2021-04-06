# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final. mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os números {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('Os números pares digitados foram ', end='')
for c in num:
    if c % 2 ==0:
        print(c, end=' ')

