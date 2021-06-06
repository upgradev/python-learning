# a sets is a set of charcters inside a pair of square brackets[] with a special meaning

import re

s = "I love watching movies"
x = re.findall("[arn]", s)
print(x)


s = "I love watching movies"
x = re.findall("[a-n]", s)
print(x)

s = "I love watching movies"
x = re.findall("[^arn]", s)
print(x)

s = "I love watching movies after 8pm"
x = re.findall("[0-9]", s)
print(x)

s = "I love watching movies"
x = re.findall("[a-zA-Z]", s)
print(x)

s = "I love watching movies +"
x = re.findall("[+]", s)
print(x)