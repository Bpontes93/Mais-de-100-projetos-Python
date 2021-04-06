# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# Perguntar o valor, salário do comprador e quantos anos ele vai pagar.
# Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do sálario para não ser negado.

print('\33[1;34;m=-\33[m' * 35)
nome = str(input('Digite seu nome: '))
valor = float(input('Digite o valor do imóvel R$ '))
salario = float(input('Digite o seu salário R$ '))
tempo = int(input('Digite em anos o tempo q deseja pagar: '))
vzs = 12 * tempo
prestacao = valor/vzs
porcentagem = (prestacao*100) / (salario)

if porcentagem <= 30.0:
    print('\33[1;32;m=-\33[m'*35)
    print('Parabéns, seu financiamento foi aprovado! sendo:')
    print('Prestação de R${:0.2f} em {:0.0f} Vezes'.format(prestacao, vzs))

else:
    print('\33[1;31;m=-\33[m' * 35)
    print('Infelizmente não foi possivel aprovar seu financiameto')

print('Valor da prestação R${:0.2f}, Porcentagem de {:0.2f}% da parcela sobre salário.'.format(prestacao, porcentagem))
print('\33[1;34;m=-\33[m' * 35)