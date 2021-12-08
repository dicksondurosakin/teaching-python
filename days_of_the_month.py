month = input("what month do you want to know? ")

if month == "september" or month == "april" or month == "june" or month =="november":
    print(f"{month} has 30 days")
elif month == "february":
    print(f"{month} has 28 or 29 days")
else:
    print(f"{month} has 31 days")
