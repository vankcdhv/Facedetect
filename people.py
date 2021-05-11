class People:
    def __init__(self, id, name, gender, age):
        self.__id = id
        self.__name = name
        self.__gender = gender
        self.__age = age
    def setID(self, id):
        self.__id = id
    def setName(self, name):
        self.__name = name
    def setGender(self, gender):
        self.__gender = gender
    def setAge(self, age):
        self.__name = age
    def getID(self):
        return self.__id
    def getName(self):
        return self.__name
    def getGender(self):
        return self.__gender
    def getAge(self):
        return self.__age
    def toString(self):
        return str(self.__id)+ " | " + self.__name + " | " + str(self.__age) + " | " + self.__gender
    