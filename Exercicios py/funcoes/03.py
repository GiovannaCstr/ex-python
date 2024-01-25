""" Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função """

def celsius_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

def farenheit_celsius(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius

resposta = int(input('Escolha a conversão: \n 1 - Celsius para Farenheit \n 2 - Farenheit para Celsius \n'))

if resposta == 1:
    celsius = float(input('Informe a temperatura para conversão: '))
    print('A temperatura convertida é: ', celsius_farenheit(celsius))
elif resposta == 2:
    farenheit = float(input('Informe a temperatura para conversão: '))
    print('A temperatura convertida é: ',farenheit_celsius(farenheit))
else:
    print('Opção inválida!')
    