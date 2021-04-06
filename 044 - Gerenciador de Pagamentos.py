# Elabore um programa que calcule o valor a ser pago por um produto.
# Considere o preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto. | À vista no cartão: 5% de desconto.
# Em até 2x no cartão: sem desconto. | 3x ou mais no cartão: 20% de juros.

print('{:=^40}'.format('LOJAS PONTES'))
preço = float(input('Preço da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual opção de pagamneto? '))
if opção == 1:
    total = preço - (preço * 10 /100)
elif opção == 2:
    total= preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:0.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:0.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('\033[1;31;mOPÇÃO INVÁLIDA de pagamento. TENTE NOVAMENTE!\033[m')
print('Sua compra de R${:0.2f} vai custar R${:0.2f} no final'.format(preço, total))