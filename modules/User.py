class User:
    def __init__(self, id_user, name, email, password, telefone, created_at):
        self.__id_user = id_user
        self.__name = name
        self.__email = email
        self.__password = password
        self.__telefone = telefone
        self.__created_at = created_at

    def get_id_user(self):
        return self.__id_user

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__password

    def get_telefone(self):
        return self.__telefone

    def get_created_at(self):
        return self.__created_at

    def set_id_user(self, id_user):
        self.__id_user = id_user

    def set_name(self, name):
        self.__name = name

    def set_email(self, password):
        self.__password = password

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_created_at(self, created_at):
        self.__created_at = created_at