#Solicite ao usuário o peso em kg e a altura em metros.
#Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso/(alturaxaltura).

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

print(f'O seu IMC é: {imc:.2f}')
