"""Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais """


frase = input('Digite uma frase: ').lower()

def contar_vogais(frase):
    vogais = ['a', 'e', 'i', 'o', 'u']
    cont = 0

    for letras in frase:
        if letras in vogais:
            cont += 1
    return cont

vogais = contar_vogais(frase)

print(f'A frase tem {vogais} vogais')