# Faça um programa que leia o sexo de uma pessoa, mas só aceit os valores 'M' ou 'F'.
# Caso esteja errado peça novamente até ter um valor correto.


sex = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Dados inválidos. Digite novamente: ')).strip().upper()[0]
if sex == 'M':
    print('Sexo MASCULINO cadastrado com sucesso')
elif sex == 'F':
    print('Sexo FEMININO cadastrado com sucesso')




