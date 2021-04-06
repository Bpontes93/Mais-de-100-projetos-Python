# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pr = float(input('\nCalcule o desconto de 5%\nDigite o valor do produto: R$'))
nv = pr - (pr * (5/100))


print('Valor sem desconto R${:.2f}\nNovo valor com desconto de 5%: R${:.2f}'.format(pr, nv))