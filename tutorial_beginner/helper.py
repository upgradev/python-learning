calculation_to_secounds = 24 * 60 * 60
name_of_unit = "secounds"

def day_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_secounds} {name_of_unit}"


def validade_and_execute(num_of_days_element):
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