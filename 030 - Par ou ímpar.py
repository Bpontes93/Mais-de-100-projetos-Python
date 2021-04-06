#Crie um programa que leia um número inteiro
#Mostre se ele é par ou ímpar
import math
num = int(input("Digite um número: "))
resultado = num % 2
if resultado == 1:
    print('SEU NÚMERO {} É IMPAR!'.format(num))

else:
    print('SEU NÚMERO {} É PAR'.format(num))