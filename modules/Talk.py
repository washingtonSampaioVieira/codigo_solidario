from .Voluntary import Voluntary


class Talk:
    def __init__(self, local, theme, size, voluntary: Voluntary):
        self.__local = local
        self.__theme = theme
        self.__size = size
        self.__voluntary = voluntary

    def get_voluntary(self):
        return self.__voluntary

    def get_local(self):
        return self.__local

    def get_theme(self):
        return self.__theme

    def get_size(self):
        return self.__size

    def set_local(self, local):
        self.__local = local

    def set_theme(self, theme):
        self.__theme = theme

    def set_size(self, size):
        self.__size = size

    def set_voluntary(self, voluntary):
        self.__voluntary = voluntary
