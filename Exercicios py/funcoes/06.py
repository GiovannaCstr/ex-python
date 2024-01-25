""" Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
"""

import random

def definir_palavra():
    palavras = ['morango', 'jabuticaba', 'banana', 'acerola', 'gato', 'cachorro', 'papagaio', 'camelo']
    return random.choice(palavras)

def exibir_palavra_secreta(palavra, letras_corretas):
    display = ""
    for letra in palavra:
        if letra in letras_corretas:
            display += letra
        else:
            display += "_"
    return display

def jogar_jogo_forca():
    palavra_secreta = definir_palavra()
    tentativas_maximas = 6
    letras_corretas = []
    tentativas_erradas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra_secreta(palavra_secreta, letras_corretas))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
        else:
            tentativas_erradas += 1
            print(f"Letra incorreta. Tentativas restantes: {tentativas_maximas - tentativas_erradas}")

        palavra_atual = exibir_palavra_secreta(palavra_secreta, letras_corretas)
        print(palavra_atual)

        if palavra_atual == palavra_secreta:
            print("Parabéns! Você acertou a palavra!")
            break

        if tentativas_erradas == tentativas_maximas:
            print("Você excedeu o número máximo de tentativas. A palavra era:", palavra_secreta)
            break

if __name__ == "__main__":
    jogar_jogo_forca()
