#Desenvolva um programa que leia o comprimento de três retas e diga se elas podem formar um triângulo.

print("=-"*20)
print("ANALISADOR DE TRIÂNGULOS")
print("=-"*20)
r1 = float(input('Digite a primeira medida: '))
r2 = float(input('Digite a segunda medida: '))
r3 = float(input('Digite a terceira mediad: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32;mPODEM\033[m formar um triângulo!')
else:
    print('OS segmentos \033[1;31;mNÃO PODEM\033[m formar um triângulo!')
