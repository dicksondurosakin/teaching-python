print("Welcome to the Basic Calculator" + "\n")
number1 = int(input("What is the first number "))
number2 = int(input("What is the second number "))

addition = number1+number2
subtraction = number1-number2
division = round(number1/number2,2)
multiplication = number1*number2

##F STRINGS
print(f"Addition = {addition}")
print(f"Subtraction = {subtraction}" )
print(f"Division = {division}" )
print(f"Multiplecasion = {multiplication}" )
