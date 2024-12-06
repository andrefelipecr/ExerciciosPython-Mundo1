from colorama import Fore, Back, Style, init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'negrito_sub': '\033[1;4m',
         'fundo_verde': '\033[42m',
         'fundo_vermelho:': '\033[41m',
         'limpa': '\033[m'}

print(f'{cores["titulo"]}======= DESAFIO 31 - PREÇO DA CORRIDA =======')

print()

km = float(input('Digite a distância da corrida em km: '))

# Usa estrutura condicional para calcular o preço da corrida
if km > 200:
    preço = km * 0.45
else:
    preço = km * 0.50

print(f'Total a pagar: {cores["negrito_sub"]}R${preço:.2f} reais{cores["limpa"]}.')
print()
print(f'{cores["fundo_verde"]}{cores["negrito_sub"]}Tenha uma boa viagem!')
