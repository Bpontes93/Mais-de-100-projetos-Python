#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1.nome completo com todas as letras maiúsculas.
#2.nome completo com todas letras minúsculas.
#3.quantas letras no total (sem considerar espaço).
#4.quantas letra o primeiro nome.

nome = str(input('Digite seu nome completo?'))
nmaiusc = nome.upper()
nminusc = nome.lower()
dividido = nome.split()
nm = nome.replace(' ','')
print('-'*50)
print('NOME COMPLETO MAIÚSC.: {}'.format(nmaiusc))
print('nome completo minúsc.: {}'.format(nminusc))
print('Possui {} letras o nome completo'.format(len(nm)))
print('Possui {} letras o primeiro nome'.format(len(dividido[0])))
print('-'*50)
