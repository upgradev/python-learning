import re

# backlash A
s = "I love watching movies"
x = re.findall("\AThe", s)
print(x)

# backslash b
s = "I love watching movies"
x = re.findall(r"\bI ", s)
print(x)

# backslash B
s = "I love watching movies"
x = re.findall("\BS", s)
print(x)

# backslash D
s = "I love watching movies"
x = re.findall("\D", s)
print(x)

# backslash d
s = "I love watching movies"
x = re.findall("\d", s)
print(x)

# backslash s white space
s = "I love watching movies"
x = re.findall("\s", s)
print(x)
