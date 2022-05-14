class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I'm  {self.name}")


person1 = Person("Tom")
person1.talk()

person2 = Person("Bob")
person2.talk()