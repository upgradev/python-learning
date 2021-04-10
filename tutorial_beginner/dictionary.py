# calculation_to_secounds = 24 * 60 * 60
# name_of_unit = "secounds"

def day_to_units(number_of_days, convertion_unit):
    if convertion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} {convertion_unit}"
    elif convertion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} {convertion_unit}"
    else:
        return "unsupported unit"

def validade_and_execute():
    # if user_input.isdigit():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = day_to_units(user_input_number, days_and_unit_dictionary["unit"])
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
    user_input =  input("hey user, enter a number of days and convert unit:\n")
    days_and_unit = user_input.split(":")
    # for num_of_days_element in user_input.split(", "):
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0] , "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validade_and_execute()

# my_list = ["20", "30", "100"]
# print(my_list[2])
#
# my_dictionary = {"days": 20 , "unit": "hours"}
# print(my_dictionary["days"])


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


