# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

from math import radians, sin, cos, tan
ag = float(input('Digite o valor do Angulo? '))
sen = sin((radians(ag)))
cos = cos(radians(ag))
tan = tan(radians(ag))
print('-' * 12)
print("O angulo de {}° corresponde á:\nSeno {:.2f}\nCosseno {:.2f}\nTangente {:.2f}".format(ag, sen, cos, tan))