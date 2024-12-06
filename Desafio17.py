print('======= DESAFIO 17 - CALCULANDO A HIPOTENUSA =======')

# Importando as funções (raiz quadrada e potenciação)
from math import pow,sqrt

op = float(input('Insira o comprimento do cateto oposto: '))
adj = float(input('Insira o comprimento do cateto adjacente: '))

# h² = c² + c²
hip = sqrt(pow(op,2) + pow(adj,2))

print()
print(f'O comprimento da hipotenusa é igual a {hip:.2f}')
