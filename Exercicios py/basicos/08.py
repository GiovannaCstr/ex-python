"""Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês"""

valor = float(input('Informe quanto você ganha por hora: ')) 
horas = float(input('Informe o número de horas trabalhadas no mês: '))

salario = valor * horas

print(f'Seu salário é de: R$ {salario:.2f}')