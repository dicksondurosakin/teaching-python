##first_dict = {"name":"Dickson",1:"Python",2:"turtle",3:"pygame","age":19}
##
##first_dict["tutor"] = "Noah"
##
##del first_dict[1]
##del first_dict[2]
##
##print(first_dict)



##dictionaries are unordered
##first_dict = {"name":"Dickson",1:"Python",2:"turtle",3:"pygame","age":19}
##second_dict = {2:"turtle",3:"pygame","age":19,"name":"Dickson",1:"Python"}
##
##print(first_dict==second_dict)






##first_dict = {"name":"Dickson",1:"Python",2:"turtle",3:"pygame","age":19}
##
##third_dict = {"name":"Dickson","subject":{1:"Python",2:"turtle",3:"pygame"},"age":19}
##
##
##print(third_dict["subject"][1])
##print(third_dict["subject"][2])
##print(third_dict["subject"][3])
##print(third_dict["age"])






##first_dict = {"name":"Dickson","subjects":["Python","turtle","pygame"],"age":19}
##second_dict = {"country":"Nigeria","city":"Lagos"}


##dict_list = [
##    {"name":"Dickson","subjects":["Python","turtle","pygame"],"age":19},
##    {"country":"Nigeria","city":"Lagos"}]

##print(first_dict["subjects"][1])
##print(dict_list[1]["city"])

##first_dict = {}
##second_dict = {}
##
##print(first_dict)
##print(second_dict)

my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}


##sum = 0
##for key in my_dict:
##    value = my_dict[key]
##    sum += value
##print(sum)



##print(list(my_dict.keys()))
values = list(my_dict.values())

sum = 0
for items in values:
    sum += items
print(sum)












