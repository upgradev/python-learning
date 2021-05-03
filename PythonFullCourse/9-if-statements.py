age = int(input("How old are you? "))

if age == 100:
    print("you are century old")
elif age >= 18:
    print("you are an adult")
elif age < 0:
    print("You haven't been born yet")
else:
    print("you are a child!")
