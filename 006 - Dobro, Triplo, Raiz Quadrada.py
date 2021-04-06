# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Esolha seu número: '))
dbr = n * 2
trp = n * 3
rz = n ** (1/2)
print('O dobro é: {}\nO triplo é: {}\nTem como raiz quadrada: {:.2f}.'.format(dbr, trp, rz))
