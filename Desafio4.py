print('================ DESAFIO 4 - TESTANDO MÉTODOS ================')
msg = (input('Digite qualquer coisa no teclado: '))
print(f'''Tipo primitivo da váriavel -> {msg.__class__}
O que você digitou tem apenas números?      -> {msg.isnumeric()}
O que você digitou tem apenas letras?       -> {msg.isalpha()}
O que você digitou tem letras e/ou números? -> {msg.isalnum()}
O que você digitou tem apenas espaços?      -> {msg.isspace()}
Você digitou tudo em letras minúsculas?     -> {msg.islower()}
Você digitou tudo em letras maiúsculas?     -> {msg.isupper()}
''')
