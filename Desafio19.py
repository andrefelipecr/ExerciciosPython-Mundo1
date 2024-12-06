# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

from random import choice

print(f'{MAGENTA}======= DESAFIO 19 - SORTEANDO ALUNOS ======={RESET}')

print()

# Ler o nome de 4 alunos
alunos = [input(f'{YELLOW}Digite o nome do 1º aluno:{RESET} '), 
          input(f'{YELLOW}Digite o nome do 2º aluno:{RESET} '), 
          input(f'{YELLOW}Digite o nome do 3º aluno:{RESET} '), 
          input(f'{YELLOW}Digite o nome do 4º aluno:{RESET} ')]

# Usar a função 'choice' para escolher entre os 4 alunos
sorteado = choice(alunos)

print()
print(f'O aluno sorteado para apagar o quadro foi {GREEN}{sorteado}{RESET}.')
