class Cat:

    def __init__(self, name, age):
        self._age = age
        self._name = name

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def __str__(self):
        return "Cat:\nName:" + self._name + "\nAge: " + str(self._age)




c1 = Cat("hello", 5)
print(c1)

c1.set_name("mawmaw")
print(c1)
