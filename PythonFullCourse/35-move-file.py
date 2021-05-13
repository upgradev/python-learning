import os

source = "test.txt"
destination = ""

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was movie")
except FileNotFoundError:
    print(source + " not found")
