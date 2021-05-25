from .User import User


class Doctor:

    def __init__(self, endereco, crm, user: User):
        self.__address = endereco
        self.__crm = crm
        self.__user = user

    def get_address(self):
        return self.__address

    def get_crm(self):
        return self.__crm

    def get_user(self):
        return self.__user

    def set_endereco(self, address):
        self.__address = address

    def set_crm(self, crm):
        self.__crm = crm

    def set_user(self, user):
        self.__user = user
