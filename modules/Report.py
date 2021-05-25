class Report:
    def __init__(self, name, url):
        self.__url = url
        self.__name = name

    def get_name(self):
        return self.__name

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def set_name(self, name):
        self.__name = name
