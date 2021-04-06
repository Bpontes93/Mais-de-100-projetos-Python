# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado.

d = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos km percorreu com o veiculo? '))
pg = (d * 60) + (km * 0.15)

print('total a pagar: R${:.2f}'.format(pg))