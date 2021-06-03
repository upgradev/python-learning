class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


p1 = Person("ana", 25)
p1.display()


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

s1 = Student("carla", 30)
s1.display()