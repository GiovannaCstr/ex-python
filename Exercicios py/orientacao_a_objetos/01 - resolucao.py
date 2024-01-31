class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('Ligado')
        else:
            print('O carro já está ligado')
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('Desligado')
        else:
            print('O carro já está desligado')
    
    def acelerar(self, velocidade):
        if not self.ligado: 
            print('O carro precisa estar ligado antes de acelerar')
        else:
            self.velocidade += velocidade
            print(f"O carro acelerou para {self.velocidade} km/h.")
    
    def desacelerar(self, velocidade):
        if self.ligado:
            if self.velocidade >= velocidade:
                self.velocidade -= velocidade
                print(f"O carro desacelerou para {self.velocidade} km/h.")
            else:
                print("O carro não pode desacelerar mais do que sua velocidade atual.")
        else:
            print("Você precisa ligar o carro antes de desacelerar.")

meu_carro = Carro(cor = 'Branco', modelo = 'Fiat')

meu_carro.ligar()
meu_carro.acelerar(20)
meu_carro.desacelerar(10)
meu_carro.desligar()