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

print(f'{cores["titulo"]}======= DESAFIO 25 - VERIFICA SE TEM "SILVA" NO NOME =======')
nome = input(f'{cores["negrito_sub"]}Digite algum nome completo:{cores["limpa"]} ').upper()
print()
# Verifica se tem "Silva" no nome
if ('SILVA' in nome) == True:
    print(f'Neste nome tem "Silva"? {cores["verde_sub"]}Verdadeiro')
else:
    print(f'Neste nome tem "Silva"? {cores["vermelho_sub"]}Falso')
