#Reverso do número. Faça uma função que retorne o reverso de um
#número inteiro informado. Por exemplo: 127 -> 721

def reverso(num):
    num_reverso = int(str(num)[::-1])
    return num_reverso

num = int(input('Digite um número: '))
print(reverso(num))