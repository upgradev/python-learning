calculation_to_secounds = 24 * 60 * 60
name_of_unit = "secounds"

def day_to_units(number_of_days):
    print(f"{number_of_days} days are {number_of_days * calculation_to_secounds} {name_of_unit}")

day_to_units(10)
day_to_units(35)
day_to_units(50)
day_to_units(100)

# print(f"35 days are {35 * calculation_to_secounds} {name_of_unit} ")
# print(f"50 days are {50 * calculation_to_secounds} {name_of_unit} ")


