# Refaça o Ex.35, acresentando o recurso mostrando qual triângulo será formado.
# Equilátero, Isósceles ou Escaleno.

print("=-"*20)
print("ANALISADOR DE TRIÂNGULOS")

r1 = float(input('Digite a primeira medida: '))
r2 = float(input('Digite a segunda medida: '))
r3 = float(input('Digite a terceira medida: '))

print("=-"*35)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32;mPODEM\033[m formar um triângulo! ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('OS segmentos \033[1;31;mNÃO PODEM\033[m formar um triângulo!')
