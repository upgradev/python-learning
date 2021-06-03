# filter (function, interable)########################
score = [76, 23, 54, 12, 65, 43]


def score_check(s):
    if s > 50:
        return True
    else:
        return False


students_passed = filter(score_check, score)
for i in students_passed:
    print(i)


# map function (function, interable)###################
total_score = [365,450,290,398,270,430]

def percent(li):
    ans = (li*100) / 500
    return ans

mapped_list = map(percent, total_score)
print(list(mapped_list))


# zip function (function, interable)###################
students_names = ["rohan", "Amita", "Shushant", "Pawan", "Kiran"]

students_marks = [67,34,78,85,65]

# zipped
zipped_list = zip(students_names, students_marks)
zipped_list = list(zipped_list)
print(zipped_list)

# unzipped
students_names, students_marks = zip(*zipped_list)
print("names: ", list(students_names))
print("marks: ", list(students_marks))