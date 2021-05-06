# str.format() =    optional method that gives users more control when displaying output

# animal = "cow"
# item = "moon"

# print("The " + animal + " jumped over the " + item)
# print("the {} jumped over the {}".format(animal, item))
# print("the {1} jumped over the {0}".format(animal, item))
# print("the {animal} jumped over the {item}".format(animal="cow", item="moon"))

# text = "the {} jumped over the {}"
# print(text.format(animal, item))

# name = "Bro"
# print("Hello my name is {}".format(name))
# print("Hello my name is {:10}. Nice to meet you".format(name))
# print("Hello my name is {:<10}. Nice to meet you".format(name))
# print("Hello my name is {:>10}. Nice to meet you".format(name))
# print("Hello my name is {:^10}. Nice to meet you".format(name))


number = 1000
print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))


