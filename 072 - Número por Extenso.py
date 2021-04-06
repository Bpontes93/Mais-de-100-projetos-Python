# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
# até vinte. O programa deve ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

nume = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número de 0 a 20 para obter sua for escrita por extenso: '))
    if 0 <= num <=20:
        print(f'Você digitou o número {nume[num]}')
    else : print('Tente Novamente. ', end='')
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if res == 'N':
        break

print('Fim')