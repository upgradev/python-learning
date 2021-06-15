var1=20

def abc():
    # local variable
    # var1 = "Python"
    
    global var1
    var1 = 50
    print(var1)

abc()
print(var1)
