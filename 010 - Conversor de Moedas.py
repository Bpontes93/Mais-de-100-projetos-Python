# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela
# pode comprar.

print('Conversor de Real em Dolár')
vl = float(input('Quanto em Real: R$'))
dl = float(3.27)
vc = vl / dl
print('Valor do Dolár em relação ao Real: R$ {}\nSeu dinheiro convertido para Dolár: {:0.2f}'.format(dl, vc))
