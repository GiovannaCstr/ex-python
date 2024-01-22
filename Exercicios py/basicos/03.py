# Faça um Programa que peça a quantidade de quilômetros, transforme
# em metros, centímetros e milímetros.

km = float(input('Informe a distância em quilômetros: '))

metros = km*1000
centimetros = metros*100
milimetros = metros*1000

print(f'{km} são equivalentes a:')
print(f'{metros} metros')
print(f'{centimetros} centímetros')
print(f'{milimetros} milímetros')
