from colorama import Fore, Back, Style, init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'negrito_sub': '\033[1;4m',
         'fundo_verde': '\033[42m',
         'fundo_vermelho:': '\033[41m',
         'branco_amarelo': '\033[33;47m',
         'invertido': '\033[7m',
         'limpa': '\033[m',
         'limpa_linha': '\033[2K',
         'volta_linha': '\033[A'}

from random import randint
from time import sleep

print(f'{cores["titulo"]}======= DESAFIO 28 - JOGO DA ADIVINHAÇÃO =======')

print()

# Sorteia um número aleatório entre 0 e 5
comp_num = randint(0, 5)

# Pede para o usuário tentar adivinhar o número sorteado
user_num = int(input(f'{cores["negrito_sub"]}Tente adivinhar o número sorteado pelo computador, entre 0 e 5:{cores["limpa"]} '))

print()

# Espera 1.5 segundos até executar o próximo comando
print(f'{cores["branco_amarelo"]}LOADING...{cores["limpa"]}{cores["volta_linha"]}{cores["limpa_linha"]}')
sleep(1.5)

# Usa estrutura condicional composta para verficar se o usuário acertou o número sorteado
if user_num >=0 and user_num <= 5:
    if user_num == comp_num:
        print(f'{cores["fundo_verde"]}{cores["negrito_sub"]}YOU WIN!{cores["limpa"]} O número sorteado foi {comp_num}')
    else:
        print(f'{cores["fundo_vermelho:"]}{cores["negrito_sub"]}YOU LOST :({cores["limpa"]}. O número sorteado foi {comp_num}.')
else:
    print('Você não digitou um número de 0 a 5. Tente outra vez.')

print(f"""
SESSÃO ENCERRADA...
{'-'*23}""")

print()
