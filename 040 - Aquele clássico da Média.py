# Crie um programa que leia dias notas de um aluno e  calcule sua média.
# Mostrando abaixo de 4.9(reprovado), 5 e 6.9(recuperação) e superior a 7 (aprovado).

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
m = (n1 + n2)/2
if m <= 4.9:
    print('Sua média é {:0.1f}! \33[1;31;mReprovado!\33[m'.format(m))

elif m <= 6.9:
    print('Sua média é {:0.1f}! \33[1;33;mRecuperação!\33[m'.format(m))

else:
    print('Sua média é {:0.1f}! \33[1;32;mAprovado!\33[m'.format(m))