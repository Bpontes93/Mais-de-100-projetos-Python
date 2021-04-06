# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

print('Olá digite suas notas de acordo com cada matéria: ')
ntp = float(input('Português: '))
ntm = float(input('Matemática: '))
md = (ntp + ntm)/2
print('Sua nota média é: {:.1f}.'.format(md))
