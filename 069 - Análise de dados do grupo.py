# Leia idade e o sexo de várias pessoas. A cada pessoa cadastraa, o programa deverá perguntar se o
# usuário quer continuar ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
i = s = sm = fm = maiores = 0

while True:
    s = str(input('Digite o Sexo: [F/M]')).upper().strip()[0]
    i = int(input('Digite a Idade: '))

    if i >= 18:
        maiores +=1
    if s in 'Mm':
        sm += 1
    if s in 'Fm':
        if i < 18:
            fm += 1

    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in "Nn":
        break


print(f'Possui {maiores} pessoas maiores de 18 anos.')
print(f'Cadastrou {sm} Homens.')
print(f'Possui {fm} mulheres com menos de 20 anos')