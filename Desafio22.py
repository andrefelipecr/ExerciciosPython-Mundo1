# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}======= DESAFIO 22 - ANALISADOR DE NOMES ======={RESET}')

print()

nome = input(f'{YELLOW}Nome Completo:{RESET} ').strip()

print()

# Mostra o nome com letras maiúsculas
print(f'{CYAN}Seu nome em Maiúsculas:{RESET} {nome.upper()}')

# Mostra o nome com letras minúsculas
print(f'{CYAN}Seu nome em Minúsculas:{RESET} {nome.lower()}')

# Conta quantos espaços tem na string
qtdEspaços = nome.count(' ')

# Determina a quantas letras tem ao todo, sem contar os espaços
qtdLetras = len(nome) - qtdEspaços

print(f'{CYAN}Seu nome completo tem {RESET}{qtdLetras} letras')

# Divide o nome em partes 
nome_dividido = nome.split()

# Mostra a quantidade de letras da primeira parte da string
print(f'{CYAN}Seu primeiro nome "{nome_dividido[0]}" tem {RESET}{len(nome_dividido[0])} letras')
