""" Escreva um programa que calcule o tempo de uma viagem.
Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração: 
● avião = 600km/h 
● carro = 100km/h 
● ônibus = 80km/h """

percurso = float(input('Informe a distância da viagem em quilômetros: '))

aviao = percurso / 600
carro = percurso / 100
onibus = percurso / 80

print(f'Tempo do percurso de:\n Avião: {aviao:.2f}\n Carro: {carro}\n Ônibus: {onibus}')


