class Person:
    def __init__(self, name):
        self.name = name
        print("initialize")

    def hello(self):
        print("HELLO " + self.name + "!")

    def goodbye(self):
        print("GOOD BYE " + self.name + "!")


person = Person("naka")
person.hello()
person.goodbye()
