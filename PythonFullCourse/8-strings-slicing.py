
name = "Bro Code"

first_name = name[: 3]
last_name = name[4:]
funny_name = name[0:8:2]
reverse_name = name[::-1]


print(first_name)
print(last_name)
print(funny_name)
print(reverse_name)

# slice

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website[slice])
print(website2[slice])