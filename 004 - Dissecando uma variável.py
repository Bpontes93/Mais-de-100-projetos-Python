# Faça um programa que leia algo pelo reclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

x = input('Digite algo? ')
print('O tipo primitivo desse valor é', type(x))
print('Só tem espaços? {}'.format(x.isspace()))
print('É um número? {}'.format(x.isnumeric()))
print('É alfabético? {}'.format(x.isalpha()))
print('É alfanumérico? {}'.format(x.isalnum()))
print('Está em maiúsculas? {}'.format(x.isupper()))
print('Está em minúsculas? {}'.format(x.islower()))
print('Está capitalizada? {}'.format(x.istitle()))

