# Python reading files
try:
    with open("./test.txt") as file:
        print(file.read())

except FileNotFoundError as e:
    print(e)
    print("that file was not found")
