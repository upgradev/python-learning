
# ---------------------------
def new_game():
    guess = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("# ---------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        question_num += 1

# ---------------------------


def check_answer():
    pass

# ---------------------------


def display_score():
    pass

# ---------------------------


def play_again():
    pass

# ---------------------------


questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()
