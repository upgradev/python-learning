
student = ("bro", 21, "male")

print(student.count("bro")) #count 
print(student.index("male")) #position

for x in student:
    print(x)

if "bro" in student:
    print("Bro is here")