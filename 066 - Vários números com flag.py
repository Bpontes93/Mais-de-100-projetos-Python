# Crie um programa que leia vários números inteiros, o programa vai parar quando o isiário digitar 999,
# que é a condição de parada, no final mostre quantos números foram digitados e qual a soma entre eles.
# desconsiderando o flag.

n = cont = soma = 0

while True:
    n = int(input('Digite um número: [999 para parar] '))
    cont += 1
    if n == 999:
        break
    soma += n
print(f'Você digitou {cont} números e a soma é {soma}')