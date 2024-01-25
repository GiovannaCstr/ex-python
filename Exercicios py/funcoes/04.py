""" Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21 """


def conversão(valor_carteira):
    dolar_americano = valor_carteira / 4.91
    peso_argentino = valor_carteira / 0.02
    dolar_australiano = valor_carteira / 3.18
    dolar_canadense = valor_carteira / 3.64
    franco_suico = valor_carteira / 0.42
    euro = valor_carteira / 5.36
    libra_esterlina = valor_carteira / 6.21
    return dolar_americano, peso_argentino, dolar_australiano, dolar_canadense, franco_suico, euro, libra_esterlina

valor_carteira = float(input('Informe o valor na carteira: '))
resultado = conversão(valor_carteira)

print('Com o valor informado seria possível comprar: ')
print(f'Dolar americano: R$ {resultado[0]:.2f}')
print(f'Peso argentino: R$ {resultado[1]:.2f}')
print(f'Dolar australiano: R$ {resultado[2]:.2f}')
print(f'Dolar canadense: R$ {resultado[3]:.2f}')
print(f'Franco suiço: R$ {resultado[4]:.2f}')
print(f'Euro: R$ {resultado[5]:.2f}')
print(f'Libra esterlina: R$ {resultado[6]:.2f}')


