from colorama import Fore, Back, Style, init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'negrito_sub': '\033[1;4m',
         'fundo_verde': '\033[42m',
         'fundo_vermelho:': '\033[41m',
         'limpa': '\033[m'}
        
from datetime import date

print(f'{cores["titulo"]}======= DESAFIO 32 - É ANO BISSEXTO? =======')

print()

ano = int(input(f"""{cores['negrito_sub']}|0| para analisar o ano atual{cores['limpa']}
Digite um ano qualquer: """))

# Se o usuário digitar '0', será verificado o ano atual |2024|
if ano == 0:
    ano = date.today().year

print()

# Verifica se o ano digitado é bissexto ou não 
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} {cores["verde_sub"]}é um ano bissexto!')
else:
    print(f'O ano de {ano} {cores["vermelho_sub"]}não é um ano bissexto!')
