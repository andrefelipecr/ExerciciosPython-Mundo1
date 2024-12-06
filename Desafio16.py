print('======= DESAFIO 16 - MOSTRA PARTE INTEIRA E DECIMAL =======')

from math import trunc

num = float(input('Digite um número com casas decimais: '))

# calcula a parte inteira
parte_inteira = trunc(num)

# calcula a parte decimal
parte_decimal = num - parte_inteira

print(f'A parte inteira de {num} é {parte_inteira}')
print(f'A parte decimal de {num} é {parte_decimal:.4}')
