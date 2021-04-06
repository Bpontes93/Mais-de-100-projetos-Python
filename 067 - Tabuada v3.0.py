# Faça um programa que mostre a tabuada de varios números, um de cada vez, para o valor digitado.
# O programa será interrompido quando o número solicitado for negativo.

n = 0

while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    c = 0
    while c < 10:
        c += 1
        print(f'{n} x {c:2} = {n*c:2}')


print('FIM')