class Voluntary:
    def __init__(self, name, cpf, telphone):
        self.__name = name
        self.__cpf = cpf
        self.__telphone = telphone

    def get_name(self):
        return self.__name

    def get_cpf(self):
        return self.__cpf

    def get_telphone(self):
        return self.__telphone

    def set_name(self, name):
        self.__name = name

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_telphone(self, telphone):
        self.__telphone = telphone
