# Peça ao usuário para informar o ano de nascimento. Em seguida,
# calcule e imprima a idade atual.

from datetime import date

anoNascimento = int(input('Informe o ano do seu nascimento: '))

idade = date.today().year-anoNascimento

print(f'Você tem {idade} anos')
