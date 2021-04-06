# A confederação de natação precisa de um programa que leia o ano de nascimento do atleta e mostre sua cat.
# Até 9 anos: Mirim | Até 14 anos: Infantil | Até 19 anos: Junior | Até 20 anos: Sênior | Acima: Master

from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento

print('Sua idade {}.'.format(idade))

if idade <= 9:
    print('Sua Categoria é \33[1;34;mMIRIM\33[m.')

if idade > 9 and idade <= 14:
    print('Sua Categoria é \33[1;34;mINFANTIL\33[m.')

if idade > 14 and idade <= 19:
    print('Sua Categoria é \33[1;34;mJÚNIOR\33[m.')

if idade == 20:
    print('Sua Categoria é \33[1;34;mSÊNIOR\33[m.')

if idade >= 21:
    print('Sua Categoria é \33[1;34;mMASTER\33[m.')