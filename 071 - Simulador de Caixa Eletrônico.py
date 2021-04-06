# Simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor ser]ao entregues
# Considerar que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


cont50 = cont20 = cont10 = cont1 = 0
print('-'*45)
print('{:^45}'.format('BANCO PONTES'))
print('-'*45)

valor = int(input('Digite o valor que deseja sacar: R$'))
montante = valor

while True:

    while montante >= 50:
        montante -= 50
        cont50 += 1
    while montante >= 20:
        montante -= 20
        cont20 += 1
    while montante >= 10:
        montante -= 10
        cont10 += 1
    while montante >= 1:
        montante -= 1
        cont1 += 1
    if montante == 0:
        break

print(f'Seu saque foi gerado, sendo:')
if cont50 > 0:
    print(f'{cont50:2} notas de R$50')
if cont20 > 0:
    print(f'{cont20:2} notas de R$20')
if cont10 > 0:
    print(f'{cont10:2} notas de R$10')
if cont1 > 0:
    print(f'{cont1:2} notas de R$1')

print('-'*45)
print('{:^45}'.format('Obrigado! Volte Sempre!'))
print('-'*45)