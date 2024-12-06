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

print(f'{cores["titulo"]}===== DESAFIO 26 - ENCONTRANDO LETRA NA FRASE =====')
frase = input(f'{cores["negrito_sub"]}Digite uma frase:{cores["limpa"]} ').upper().strip()

print()

# Usa o métdodo count() para contar quantas letras 'a' aparecem na frase
print(f'Quantas vezes a letra {cores["negrito_sub"]}"a"{cores["limpa"]} aparece na frase: {frase.count("A")}')


# Usa o método find() para analisar em qual posição aparece a letra 'a' pela primeira vez
print(f'Em qual posição aparece a letra {cores["negrito_sub"]}"a"{cores["limpa"]} pela primeira vez: {frase.find("A") + 1}')

# Usa o método rfind() para analisar, da direita para a esquerda, a posição da letra 'a'
print(f'Em qual posição aparece a letra {cores["negrito_sub"]}"a"{cores["limpa"]} pela última vez: {frase.rfind("A") + 1}')
