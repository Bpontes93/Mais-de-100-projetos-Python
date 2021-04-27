# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em
# um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
# todas as pessoas cadastradas.
from ex115.lib.arquivo import *
from ex115.lib.interface import *
from ex115.lib.cores import *
from time import sleep
arq = 'Dados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
        r = abrirMenu('Deseja abrir o menu? [Sim/Não] ')
        if r == 'N':
            fechaPrograma(True)
            break

    elif resposta == 2:
        # Opção de adicionar conteúdo no arquivo
        cabeçalho('NOVO CADASTRO')
        novoitem = list()
        nome = str(input('Nome: ').capitalize())
        idade = leiaInt('Idade: ')
        salvarArquivo(arq, nome, idade)
        r = abrirMenu('Deseja abrir o menu? [Sim/Não] ')
        if r == 'N':
            fechaPrograma(True)
            break

    elif resposta == 3 or r == 3:
        fechaPrograma(True)
        break
    else:
        cabeçalho(vermelho('ERRO! Digite uma opção válida!'))
        sleep(0.3)
