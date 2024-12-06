from colorama import init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'negrito_sub': '\033[1;4m',
         'limpa': '\033[m'}

print(f'{cores["titulo"]}======= DESAFIO 34 - AUMENTO SALARIAL =======')

print()

salario = float(input('Digite o seu salário atual: R$'))

# Usa estrutura condicional para rajustar o sálario de um funcionário
if salario > 1250:
    print(f'Você foi promovido e terá um reajuste no salário! {cores["verde_sub"]}+10%')
    novo_salario = salario * 1.10
else:
    print(f'Você foi promovido e terá um reajuste no salário! {cores["verde_sub"]}+15%')
    novo_salario = salario * 1.15

print()

print(f'{cores["negrito_sub"]}Seu novo salário é R${novo_salario:.2f} reais.')
