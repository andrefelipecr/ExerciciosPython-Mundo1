# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

from random import sample

print(f'{MAGENTA}======= DESAFIO 20 - ORDEM DOS ALUNOS ======={RESET}')

print()

# Ler o nome de 4 alunos
alunos = [input(f'{YELLOW}Nome do 1º aluno:{RESET} '), 
          input(f'{YELLOW}Nome do 2º aluno:{RESET} '), 
          input(f'{YELLOW}Nome do 3º aluno:{RESET} '), 
          input(f'{YELLOW}Nome do 4º aluno: {RESET}')]

# Embaralha a ordem dos alunos
ordem = sample(alunos, 4)

print()
print(f'{CYAN}Ordem de apresentação dos trabalhos:{RESET}')
print()
print(f'1º {ordem[0]}')
print(f'2º {ordem[1]}')
print(f'3º {ordem[2]}')
print(f'4º {ordem[3]}')
