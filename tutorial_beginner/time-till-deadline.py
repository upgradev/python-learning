import datetime
user_input = input("Enter your goal with a dealine separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_data = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_data - today_date
print(f"Dear user, time remaining for your goal: {time_till}")
