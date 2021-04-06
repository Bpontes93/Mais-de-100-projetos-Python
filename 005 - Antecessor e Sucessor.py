# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n= int(input('Olá, digite seu número: '))
ant = n - 1
suc = n + 1
print('Seu Antecessor é: {} e seu Sucessor é: {}'.format(ant, suc))