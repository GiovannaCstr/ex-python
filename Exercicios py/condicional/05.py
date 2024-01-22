""" Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas """

ladoA = float(input('Informe o comprimento do lado A: '))
ladoB = float(input('Informe o comprimento do lado B: '))
ladoC = float(input('Informe o comprimento do lado C: '))

if ladoA == ladoB and ladoB == ladoC:
    print('Equilátero')
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print('Isóceles')
else: 
    print('Escaleno')