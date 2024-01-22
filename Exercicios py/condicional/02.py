"""Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso"""

turno = input('Em qual turno que você estuda? Digite: \n M - para matutino\n V - para vespertino\n N - para noturno\n')

if turno == "M" or turno == "m":
    print('Bom dia!')
elif turno == "V" or turno == "v":
    print('Boa tarde!')
elif turno == "N" or turno == "n":
    print('Boa noite!')
else:
    print('Valor inválido')