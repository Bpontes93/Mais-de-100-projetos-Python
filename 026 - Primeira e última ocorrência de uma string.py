#Faça um programa que leia uma frase pelo teclado e mostre:
#1.Quantas vezes aparece a letra "A".
#2.Em que posição ela aparece a primeira vez.
#3.Em que posição ela aparece a última vez.
f = str(input('Escreva sua frase ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(f.count('A')))
print('Primeira vez que aparece {}'. format(f.find('A')+1))
print('Ultima vez que aparece {}'.format(f.rfind('A')+1))