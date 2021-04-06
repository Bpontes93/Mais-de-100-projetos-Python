# Leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.


cont = total = contt = 0
barato = ''
while True:
    produto = str(input('Qual o Produto? '))
    preço = float(input('Qual o valor do produto? '))
    contt += 1
    if contt == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    if preço > 1000:
        cont += 1
    total += preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == "N":
        break



print(f'Total da compra {total:2}.\n{cont} Produtos custam mais de R$1000.00.\nO produto mais barato é {barato} por R${menor:2}.')