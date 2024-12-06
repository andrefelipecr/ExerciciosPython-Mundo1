from colorama import Fore, Back, Style, init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'negrito_sub': '\033[1;4m',
         'fundo_verde': '\033[42m',
         'fundo_vermelho:': '\033[41m',
         'invertido_sub': '\033[1;4;7m',
         'limpa': '\033[m'}

print(f'{cores["titulo"]}======= DESAFIO 27 - PRIMEIRO E ÚLTIMO NOME =======')

print()

nome = input(f'{cores["negrito_sub"]}Digite seu nome completo:{cores["limpa"]} ').split()
print() 

# Mostra o primeiro nome
print(f'Seu primeiro nome: {cores["invertido_sub"]}{nome[0]}')

#mostra o último nome
print(f'Seu último nome: {cores["invertido_sub"]}{nome[-1]}')
