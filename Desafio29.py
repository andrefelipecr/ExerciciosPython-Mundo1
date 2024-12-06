from colorama import Fore, Back, Style, init
init(autoreset=True)

cores = {'titulo': '\033[1;36m',
         'verde_sub': '\033[4;32m',
         'vermelho_sub': '\033[4;31m',
         'negrito_sub': '\033[1;4m',
         'fundo_verde': '\033[42m',
         'fundo_vermelho:': '\033[41m',
         'branco_vermelho': '\033[1;31;47m',
         'invertido': '\033[7m',
         'limpa': '\033[m'}

print(f'{cores["titulo"]}======= DEASAFIO 29 - RADAR DE VELOCIDADE =======')
print(f"""Você está dirigindo seu carro numa estrada...
De repente, passa por um radar de velocidade: {cores['branco_vermelho']}|80km/h|
""")

v = int(input('Velocidade do veículo em km/h: '))

# Usa estrutura condicional para verificar se está, ou não, acima da velocidade
if v > 80:
    multa = (v - 80) * 7.00
    print(f'{cores["fundo_vermelho:"]}ATENÇÃO{cores["limpa"]}: Você excedeu o limite de velocidade!')
    print(f'MULTA POR IMPRUDÊNCIA E EXCESSO DE VELOCIDADE: {cores["negrito_sub"]}R${multa:.2f} reais')    
else:
    print(f'{cores["fundo_verde"]}{cores["negrito_sub"]}TENHA UMA BOA VIAGEM!')

print()
