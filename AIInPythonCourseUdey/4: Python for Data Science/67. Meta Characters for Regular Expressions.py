# meta character building blocks for regular expressions

import re

# square brakcets
s = "ac"
print(re.search('[abc]', s))

# period
s = "ac"
print(re.search('.', s))

# ^ caret
s = 'mumbai'
x = re.search('^m', s)
print(x)

# dollar
a = re.search('a$', 'Delphi')
print(a)
b = re.search('a$', 'Odissa')
print(b)

# star
a = re.search('ma*', 'man')
print(a)
b = re.search("ma*", "woman")
print(b)

# plus
a = re.search('ma+', 'man')
print(a)
b = re.search("ma+", "woman")
print(b)

# braces
a = re.search('a{2}', 'abc')
print(a)
b = re.search("a{2}", "aab")
print(b)

# vertical bar
a = re.search('a|b', 'mango')
print(a)
b = re.search("a|b", "Pune")
print(b)

# parenthesis
a = re.search('(a)m', 'amm')
print(a)
b = re.search("(a)m", "abm")
print(b)

#backslash
a = re.search('\$a', '$abc')
print(a)
