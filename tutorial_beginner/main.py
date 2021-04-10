calculation_to_secounds = 24 * 60 * 60
name_of_unit = "secounds"

def day_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_secounds} {name_of_unit}"


def validade_and_execute():
    # if user_input.isdigit():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = day_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("Your input is 0. ")
        else:
            print("you entered a negative number, no convertion for you")
    # else:
    except ValueError:
        print("Your input is invalid a number. ")





user_input = ""
while user_input != "exit":
    user_input =  input("hey user, enter a number of days and i will convert it to hours:\n")
    list_of_days = user_input.split(", ")
    print(type(user_input.split(", ")))
    print(user_input.split(", "))
    # for num_of_days_element in user_input.split(", "):
    for num_of_days_element in set(list_of_days):
        validade_and_execute()





# day_to_units(20)
# day_to_units(35)
# def scope_check(num_of_days):
#     my_var = "variable inside function"
#     print(name_of_unit)
#     print(num_of_days)
#     print(my_var)

# scope_check(25)
# day_to_units(35, "Looks good!")
# print(f"35 days are {35 * calculation_to_secounds} {name_of_unit} ")
# print(f"50 days are {50 * calculation_to_secounds} {name_of_unit} ")


