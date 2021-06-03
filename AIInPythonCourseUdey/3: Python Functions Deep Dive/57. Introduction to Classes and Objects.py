#classes and objects

#class is a blueprint for objects
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    


p1 = Person("Nikhil", 20)
print(p1.name)
print(p1.age)

p1.age = 30

print(p1.name)
print(p1.age)
