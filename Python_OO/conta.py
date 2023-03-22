class Conta:

    #para deixar o atributo privado usamos (__)
    # O "self" irá ser a conta atual
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    # um metodo - conta - valor a ser transferido - destino do dinheiro
    #conta ( conta2 ) - valor para transferir ( R$ 10,00 ) - destino ( conta 1 )
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # "get" para devolver/retornar o que é pedido ( saldo, titular, limite e etc...)
    # "@property" se trata de uma propriedade então não precisa usar os () para chama-lo ELE É OS GET's
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    #"set" para receber/alterar algo
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
