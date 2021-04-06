# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
a = str(input('Primeiro aluno? '))
b = str(input('Segundo aluno? '))
c = str(input('Terceiro aluno? '))
d = str(input('Quarto aluno? '))
lista = [a, b, c, d]
e = choice(lista)
print('o aluno é {}'.format(e))