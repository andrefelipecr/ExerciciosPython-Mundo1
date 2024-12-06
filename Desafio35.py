from colorama import init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'limpa': '\033[m'}

print(f'{cores["titulo"]}======= DESAFIO 35 - PODEM FORMAR UM TRIÂNGULO? =======')

print()

r = float(input('Digite o comprimento da 1ª reta: '))
s = float(input('Digite o comprimento da 2ª reta: '))
t = float(input('Digite o comprimento da 3ª reta: '))

print()

# Usa estrutura condicional para verificar se as três retas podem formar um triângulo
if (r < s + t) and (s < r + t) and (t < r + s):
    print(f'Os valores de retas [{r}]; [{s}] e [{t}] {cores["verde_sub"]}podem formar um triângulo{cores["limpa"]}.')
else:
    print(f'Os valores de retas [{r}]; [{s}] e [{t}] {cores["vermelho_sub"]}não formam um triângulo{cores["limpa"]}.')
