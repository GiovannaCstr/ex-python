# Receba do usuário a quantidade de litros de combustível consumidos e
# a distância percorrida. Calcule e imprima o consumo médio em km/l.

combustivel = float(input('Informe a quantidade de litros de combustível consumidos: '))
distancia = float(input('Informe a distância percorrida: '))

media = combustivel / distancia

print(f'O consumo médio é de {media} km/L')