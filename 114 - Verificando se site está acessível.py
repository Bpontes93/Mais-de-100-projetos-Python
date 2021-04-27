# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.UrlError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
