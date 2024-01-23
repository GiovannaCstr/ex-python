""" O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos. """

pares = 0
impares = 0

while True:
    num = int(input('Digite um número (ou digite 0 para encerrar): '))
    if num == 0:
        break
    
    if num > 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        print('Digite somente números positivos.')        

print(f'Você digitou {pares} números pares')
print(f'Você digitou {impares} números ímpares')