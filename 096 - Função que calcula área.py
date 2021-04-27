# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (Largura e comprimento) e mostre a área do terreno.


def área(comp, larg):
    area = comp * larg
    print(f"Área de {area:0.2f} m²")


print('Digite a dimensão do terreno e descubra sua área m²')
comp = float(input("Comprimento: "))
larg = float(input("Largura: "))
área(comp, larg)
