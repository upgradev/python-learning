
import re

# findall()
st = "India is my country"
x = re.findall("nd", st)
print(x)

# search()
st = "India is my country"
x = re.search("Delhi", st)
print(x)
 
#  split
st = "I love watching movies"
x = re.split("\s", st)
print(x)

# sub replace spaces
st = "India is my country"
x = re.sub("\s", "2", st)
print(x)


