class Reception:
    def __init__(self, name, address, diagnosis):
        self.__name = name
        self.__address = address
        self.__diagnosis = diagnosis

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_diagnosis(self):
        return self.__diagnosis

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis
