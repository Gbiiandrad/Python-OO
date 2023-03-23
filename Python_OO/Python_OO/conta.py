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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Você realizou um saque de R$ {}. Seu saldo atual é de R$ {}".format(valor, self.__saldo))
        else:
            print("O valor de R$ {} passou do limite de saque da sua conta que é de {}. Por favor tentar novamente mais tade!".format(valor, self.__limite))

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

    # O "@staticmethod" Pegar o codigo do banco sem precisar criar uma conta diretamente é so tirar o "self" que nesse caso representa uma conta

    @staticmethod
    def codigo_banco():
        return "001"
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'} # assim vc poderá pegar o codigo tambem pelo nome do banco apenas
