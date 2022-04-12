class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if value == "Ram":
            self.__name = "Ram Default"
        else:
            self.__name = value

p1 = Person("Ishwar", 29, 'M')
print(p1.Name)

p1.Name = "Ram"
print(p1.Name)