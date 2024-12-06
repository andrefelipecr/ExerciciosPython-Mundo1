from colorama import init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'negrito_sub': '\033[1;4m',
         'fundo_verde': '\033[42m',
         'fundo_vermelho:': '\033[41m',
         'limpa': '\033[m'}

print(f'{cores["titulo"]}======= DESAFIO 33 - MAIOR E MENOR NÚMERO =======')
print()

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
maior = 0
menor = 0
print(f'{"-"*26}')

# Usa estrutura condicional para verificar qual número é maior
if (n1 > n2) and (n1 > n3):
    maior = n1
elif (n2 > n1) and (n2 > n3):
    maior = n2
else:
    maior = n3

# Usa estrutura condicional para verificar qual número é menor
if (n1 < n2) and (n1 < n3):
    menor = n1
elif (n2 < n1) and (n2 < n3):
    menor = n2
else:
    menor = n3

print(f'O {cores["fundo_verde"]}maior{cores["limpa"]} número é {cores["verde_sub"]}{maior}{cores["limpa"]}.')
print(f'O {cores["fundo_vermelho:"]}menor{cores["limpa"]} número é {cores["vermelho_sub"]}{menor}{cores["limpa"]}.')
print(f'{"-"*26}')
