# and or

temp = int(input("What is the temperatur outside? "))

if not(temp >= 0 and temp <= 30):
    print("temperature is bad today")
    print("stay inside")
elif not(temp < 0 or temp > 30):
    print("the temperature is goog today")
    print("go outside")
