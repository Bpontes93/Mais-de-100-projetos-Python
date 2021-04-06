#Desenvolva um programa que pergunte a distância de uma viagemem Km.
#Calcule o preço da passagem sendo: R$0,50 por Km para viagens até 200Km e R$0,45 viagens mais longas.
km = float(input("Informe a distância até o destino: "))

if 200>= km:
    print('O valor da sua viagem será de R${:0.2f}. Sendo R$0,50 por Km'.format(km * 0.50))

else:
    print('O valor de sua viagem será de R${:0.2f}. Sendo R$0,45 por Km;'.format(km * 0.45))