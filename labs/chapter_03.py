#labs/chapter_03.py

# Define counter variables
correct_answers = 0
total_questions = 0

print("== Quiz time!! ==")

# Enter question 1
question_1 = int(input("How many books are in Harry Potter? "))
if question_1 == 7:
    print("Correct!")
    
    # Increase correct answer counter
    correct_answers += 1
else:
    print("Sorry, incorrect")

# Increase total answer counter
total_questions += 1
print("************************")

# Enter question 2
question_2 = int(input("What is 1 + 1? "))
if question_2 == 2:
    print("Correct!")

    # Increase correct answer counter
    correct_answers += 1
else:
    print("Sorry, incorrect")

# Increase total answer counter
total_questions += 1
print("************************")

# Enter question 3
question_3 = str(input("What does NBA stand for? "))
if question_3.lower() == "national basketball association":
    print("Correct!")

    # Increase correct answer counter
    correct_answers += 1
else:
    print("Sorry, incorrect")

# Increase total answer counter
total_questions += 1
print("************************")

# Enter question 4
question_4 = str(input("What does USA stand for? "))
if question_4.lower() == "united states of america":
    print("Correct!")

    # Increase correct answer counter
    correct_answers += 1
else:
    print("Sorry, incorrect")

# Increase total answer counter
total_questions += 1
print("************************")

# Print question 5
print("What is on an apple tree?", end = "\n")
print("a) Grapes")
print("b) Bananas")
print("c) Apples")
print("d) Pineapples")

# Ask for answer of question 5
question_5 = input("Please choose a, b, c, d: ")

# Check answer
if question_5 == "c" or question_5 == "C":
    print("Correct!")

    # Increase correct answer counter
    correct_answers += 1
else:
    print("Sorry, incorrect")

# Increase total answer counter
total_questions += 1
print("************************")

# Questions correct
print(f'You got {correct_answers} questions correct!!')

# Calculate final score
final_score = (correct_answers / total_questions) * 100
final_score = "{:.2f}".format(final_score)
print(f'== Your final score is {final_score}% ==')
