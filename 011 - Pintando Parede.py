# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

print('\n\nCalcule a quantidade de tinta necessaria para pintar sua parede!')
a = float(input('Digite a altura de sua parede em metros: '))
l = float(input('Digite a largura de sua paredeem metros: '))
ar = a * l
tn = ar / 2

print('É necessário {} Litros de tinta para Pintar a área de {}m² de sua parede'.format(tn, ar))
