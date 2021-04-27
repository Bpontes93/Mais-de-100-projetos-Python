# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.


def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos  alunos (aceota/várias)
    :param sit: valor opicional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    r = dict()
    r['TOTAL'] = len(n)
    r['MAIOR'] = max(n)
    r['MENOR'] = min(n)
    r['MÉDIA'] = sum(n)/len(n)

    if sit:
        if r['MÉDIA'] >= 7:
            r['SITUAÇÃO'] = 'APROVADO'
        elif r['MÉDIA'] >= 5:
            r['MÉDIA'] = 'RECUPERAÇÃO'
        else:
            r['MÉDIA'] = 'REPROVADO'
    return r

resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)