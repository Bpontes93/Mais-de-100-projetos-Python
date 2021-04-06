# Faça un programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

import math
cop = float(input('Qual a medida do cateto oposto? '))
cad = float(input('Qual a medida do cateto adjacente? '))

print('A hipotenusa corresponde {:.2f}'.format(math.hypot(cop , cad)))