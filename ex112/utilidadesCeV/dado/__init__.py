# Dentro do pacote utilidades CeV que criamos no desafio 111, temos um módulo chamado dao.
#  Crie uma função chamada leiadinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitas apenas valores que sejam monetários.


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO:\"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)

def leiaPorcento(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO:\"{entrada}\" é um número inválido!\033[m')
        else:
            válido = True
            return int(entrada)
