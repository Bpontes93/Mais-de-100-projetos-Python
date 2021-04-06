#Faça um programa que leia três numeros e mostre qual é o maior e o menor.
a = int(input('DIGITE O NÚMERO 1: '))
b = int(input('DIGITE O NÚMERO 2: '))
c = int(input('DIGITE O NÚMERO 3: '))

#Verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor é {}\nO maior valor é {}'.format(menor, maior))
