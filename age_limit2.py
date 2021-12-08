user_age = int(input("What is your age? "))

if user_age >= 7 and user_age <= 18:
    print("you can attend the python for kids class")
elif user_age >= 19 and user_age <= 40:
    print("you can attend the python for youth class")
elif user_age >40:
    print("you can attend the python for adult class")
else:
    print("you can't attend any of the classes")
