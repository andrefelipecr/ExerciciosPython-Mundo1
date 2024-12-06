from colorama import Fore, Back, Style, init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'negrito_sub': '\033[1;4m',
         'fundo_verde': '\033[42m',
         'fundo_vermelho:': '\033[41m',
         'invertido': '\033[1;7m',
         'limpa': '\033[m'}

print(f'{cores["titulo"]}====== DESAFIO 24 - VERIFICA PRIMEIRO NOME DA CIDADE ======')

cidade = input(f'{cores["negrito_sub"]}Digite o nome de uma cidade:{cores["limpa"]} ').upper()

cidade_dividido = cidade.split()

print()

# Verifica se o nome da cidade começa com 'Santa'
if ('SANTA' in cidade_dividido[0]) == True:
    print(f'O nome da cidade começa com {cores["negrito_sub"]}"Santa"{cores["limpa"]}? {cores["verde_sub"]}Verdadeiro')
else:
    print(f'O nome da cidade começa com {cores["negrito_sub"]}"Santa"{cores["limpa"]}? {cores["vermelho_sub"]}Falso')
