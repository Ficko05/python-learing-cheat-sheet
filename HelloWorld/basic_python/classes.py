class Point:

    def __init__(self, x, y):  # init is shot for initialize
        self.x = x  # self is a reference to the current object
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)


#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)

class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hello your name is {self.name}")

    def talk1(self, name):
        print(f"hello your name is {name}")


person = Person("Hamlet")
person.talk1(name="peter")
person.talk()

bob = Person("bob")
bob.talk()
