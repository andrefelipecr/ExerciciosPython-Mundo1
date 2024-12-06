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

print(f'{cores["titulo"]}======= DESAFIO 30 - PAR OU ÍMPAR =======')
print()

num = int(input(f'{cores["negrito_sub"]}Digite um número:{cores["limpa"]} '))

print()

# Usa estrutura condicional composta para verificar se o número é par ou ímpar
if num == 0:
    print(f'O número {num} é {cores["invertido"]}nulo!')
elif num % 2 == 0:
    print(f'O número {num} é {cores["invertido"]}par!')
else:
    print(f'O número {num} é {cores["invertido"]}ímpar!')
