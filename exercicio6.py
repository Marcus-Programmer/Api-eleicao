class Veiculo:

    def __init__(self, marca, cor, estilo, motorLigado, enchePortaMalas):
        self.__marca = marca
        self.__cor = cor
        self.__estilo = estilo
        self.__motorLigado = motorLigado
        self.__enchePortaMalas = enchePortaMalas
    
    def ligaMotor(self):
        if self.__motorLigado == True:
            print('O motor já está ligado!')
        else:
            self.__motorLigado = True
            print('O motor acaba de ser ligado!')

    def colocarPortaMalas(self):
        if self.__enchePortaMalas == True:
            print('Seu porta malas já está cheio!')
        else:
            self.__enchePortaMalas = True
            print('Você encheu o porta malas!')

    def mostraAtributosM(self):
        print('Esta motocicleta é uma {} {} {}'.format(
            self.__marca, self.__cor, self.__estilo))
        if (self.__motorLigado):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')
    
    def mostraAtributosC(self):
        print('Este carro é um {} {} {}'.format(
            self.__marca, self.__cor, self.__estilo))
        if (self.__motorLigado):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')
        if (self.__enchePortaMalas):
            print('Seu porta malas está cheio')
        else:
            print('Seu porta malas está vazio')

   


class Moto(Veiculo):

    def __init__(self, marca, cor, estilo, motorLigado, enchePortaMalas):
         super().__init__(marca, cor, estilo, motorLigado, enchePortaMalas)

  

    


class Carro(Veiculo):

    def __init__(self, marca, cor, estilo, motorLigado, enchePortaMalas):
        super().__init__(marca, cor, estilo, motorLigado, enchePortaMalas)


   

    


moto1 = Moto('Honda', 'Vermelho', 'trail', False, False)
moto1.ligaMotor()
print()
moto1.mostraAtributosM()
print()
print()
print()
carro1 = Carro('Fiat', 'Preto', 'naked', False, False)
carro1.colocarPortaMalas()
print()
carro1.ligaMotor()
print()
carro1.mostraAtributosC()
