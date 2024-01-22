# Desenvolver um programa que solicite a idade do usuário e identifique se
# ele é uma criança, um adolescente, adulto ou idoso.


idade = int(input('Informe sua idade: '))

if idade >= 1 and idade <= 12:
    print('Criança')
elif idade > 12 and idade < 18:
    print('Adolescente')
elif idade >= 18 and idade < 60:
    print('Adulto')
elif idade >= 60:
    print('Idoso')
else:
    print('Inválido')
