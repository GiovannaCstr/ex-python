""" Escreva um programa que calcule o salário líquido. 
Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
● Renda até R$1.903,98: isento de imposto de renda;
● Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%;
● Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%; 
● Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%; 
● Renda acima de R$4.664,68: alíquota máxima de 27,5% """

salario = float(input('Informe o valor bruto do salário: '))

if salario <= 1903.98:
    liquido = salario
elif salario <= 2826.65:
    liquido = salario - (salario * 0.075) 
elif salario <= 3751.05:
    liquido = salario - (salario * 0.15)
elif salario <= 4664.68:
    liquido = salario - (salario * 0.225)
else:
    liquido = salario - (salario * 0.275)    

print(f'Salário líquido de: {liquido}')