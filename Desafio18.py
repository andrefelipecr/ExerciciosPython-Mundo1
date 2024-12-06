# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

from math import sin, cos, tan, radians

print(f'{MAGENTA}======= DESAFIO 18 - SENO, COSSENO E TANGENTE ======={RESET}')

print()

ang = int(input(f'{YELLOW}Insira o valor de um ângulo:{RESET} '))

# Converte o valor para radianos
ang_rad = radians(ang)

print()
print(f'Seno de {ang}°     = {sin(ang_rad):.2f}')
print(f'Cosseno de {ang}°  = {cos(ang_rad):.2f}')
print(f'Tangente de {ang}° = {tan(ang_rad):.2f}')
