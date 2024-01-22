"""Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício"""

horas = float(input('Informe o número de horas de exercício por semana: '))

calorias_queimadas = 5 * (horas * 60 * 4)

print(f'Você queimou um total de {calorias_queimadas} calorias')