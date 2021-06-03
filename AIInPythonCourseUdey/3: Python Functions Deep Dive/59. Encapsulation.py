# encapsulation restric direct access to methods and variable
class Person:
    def __init__(self, name, _age):
        self.name = name
        self._age = _age

    def display(self):
        print(self.name, self._age)


p1 = Person("ana", 25)
p1.display()

p1.age =36
p1.display()