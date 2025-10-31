class Person:
    def __init__(self, name_param):
        self.name = name_param
        print("I'm created.", self, self.name)

    def talk(self):
        print("Hi, I'm", self.name)

person_1 = Person("유재석")
person_1.talk()

person_2 = Person("박명수")
person_2.talk()