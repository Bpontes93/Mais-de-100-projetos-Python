#Escreva um programa que leia a velocidade de um carro.
#Se ultrapassar 80km/h. Mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite
vel = int(input('Qual a velocidade do veículo? '))
multa = (vel - 80)
if vel>80:
    print('Sua velocidade acima do permitido é {}\nVocê foi multado em R${:0.2f}'.format(multa, (multa*7)))
else:
    print('Obrigado! continue respeitando as leis de Trânsito')