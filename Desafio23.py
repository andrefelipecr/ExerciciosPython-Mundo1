# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}======= DESAFIO 23 - UNIDADE, DEZENA, CENTENA E MILHAR ======={RESET}')

print()

num = int((input(f'{YELLOW}Digite um número entre 0 e 9999:{RESET} ')))

# Atribuições - Unidade, dezena, centena e milhar
un = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10

print(f"""
{'='*26}
   Número digitado: {GREEN}{num}{RESET}
{'='*26}
|{CYAN}Unidade: {un:13}  {RESET}|
|{CYAN}Dezena:  {dez:13}  {RESET}|
|{CYAN}Centena: {cent:13}  {RESET}| 
|{CYAN}Milhar:  {mil:13}  {RESET}|
{'-'*26}""")
