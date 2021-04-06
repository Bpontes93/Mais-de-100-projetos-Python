# Escreva um programa que converta uma temperatura digitada em °C e converta para °F e ºK.


c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
k = c + 273.15

print('A temperatura de {}°C,corresponde a {}°F e {}°K'.format(c, f, k))