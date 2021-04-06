# Refaça o ex.009, mostrando a tabuada de um número que o usuário escolher, só utilizando um laço For.

n = int(input('Insira um número para obter sua tabuada: '))

for c in range (1 , 11):
    print('{} x {:2} = {}'.format(n , c, (n*c)))