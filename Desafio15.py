print('======= DESAFIO 15 - ALUGUEL DE CARROS =======')

dias = int(input('Quantos dias foram alugados? '))
km = float(input('Quantos quilômetros você percorreu com o carro? '))

# Calcula o preço total. R$60,00 por dia e R$0,15 por km rodados.
total = 60*dias + 0.15*km

print()
print(f'Total a pagar: R${total:.2f}')
