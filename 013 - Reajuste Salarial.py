# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sl = float(input('Digite seu salário: R$'))
am = sl * (15/100)
slf = sl + am

print('Aumento de R${:.2f}\nSalario futuro R${:.2f}'.format(am, slf))
