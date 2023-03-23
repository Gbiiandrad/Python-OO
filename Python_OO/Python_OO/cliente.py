class Cliente:

    # para deixar o atributo privado usamos (__)
    def __init__(self, nome):
        self.__nome = nome

    # "title" para trazer com a primeira letra maiúscula
    # "@property" se trata de uma propriedade então não precisa usar os () para chama-lo
    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome

