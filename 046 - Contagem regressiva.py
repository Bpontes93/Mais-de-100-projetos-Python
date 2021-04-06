# Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pauda de um segundo entre eles.

from time import sleep
import emoji

for c in range (10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BUM! BUM! POOW!\n:fireworks::fireworks::fireworks::fireworks::fireworks:', use_aliases=True))