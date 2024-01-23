"""Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino".
Caso contrário,ele será classificado como "Inocente". """

perguntas = ['Telefonou para a vítima?', 
             'Esteve no local do crime?', 
             'Mora perto da vítima?',
             'Devia para a vítima?',
             'Já trabalhou com a vítima?']

resposta_positiva = 0
resposta_negativa = 0

for pergunta in perguntas:
    print(pergunta)
    resposta = input('Responda "sim" ou "não": ').lower()

    if resposta == 'sim':
        resposta_positiva += 1
    elif resposta == 'não':
        resposta_negativa += 1
    else:
        print('Resposta inválida!')


if resposta_positiva == 2:
    print('Suspeito')
elif resposta_positiva >= 3 and resposta_positiva <= 4:
    print('Cúmplice')
elif resposta_positiva == 5:
    print('Assassino')
else: 
    print('Inocente')