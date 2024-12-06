print('======= DESAFIO 15 - CONVERSOR DE TEMPERATURAS =======')

C = float(input('Informe a temperatura em °C: '))
F = (9/5 * C) + 32
K = C + 273.15

print(f'A temperatura de {C}°C convertida em:')
print()
print(f'Fahrenheit -> {F:.1f}°F. \nKelvin    -> {K:.1f}K.')
