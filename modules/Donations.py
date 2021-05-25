class Donations:
    def __init__(self, value, contact, cpf, cnpj):
        self.__value = value
        self.__contact = contact
        self.__cpf = cpf
        self.__cnpj = cnpj

    def get_value(self):
        return self.__value

    def get_contact(self):
        return self.__contact

    def get_cpf(self):
        return self.__cpf

    def get_cnpj(self):
        return self.__cnpj

    def set_value(self, value):
        self.__value = value

    def set_contact(self, contact):
        self.__contact = contact

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj


