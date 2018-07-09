# # Name:
# # Date:
#
# # proj01: A Simple Program
#
# # Part I:
# # This program asks the user for his/her name and grade.
# #Then, it prints out a sentence that says the number of years until they graduate.
#
user_name = raw_input("Enter your name: ")
user_grade = raw_input("Enter the grade level you will be going into: ")

print "You will graduate from high school in", 13 - int(user_grade), "years!"


# # Part II:
# # This program asks the user for his/her name and birth month.
# # Then, it prints a sentence that says the number of days and months until their birthday
#
#
# # If you complete extensions, describe your extensions here!
user_age = raw_input("Enter your age: ")
if int(user_age) > 16:
    print "You can drive!"
elif int(user_age) == 16:
    print "You can drive in some states!"
elif int(user_age) > 95:
    print "You are too old to drive"
else:
    print "You cannot drive"
if int(user_age) < 6:
    print "You may watch G rated movies."
if 6 < int(user_age) < 13:
    print "You may watch PG rated movies."
if 13 < int(user_age) < 17:
    print "You may watch PG-13 rated movies."
if int(user_age) == 17 or int(user_age) > 17:
    print "You may watch R rated movies."
if int(user_age) == 18 or int(user_age) > 18:
    print "You can legally vote."
elif int(user_age) < 18:
    print "You cannot vote."
if int(user_age) == 21 or int(user_age) > 21:
    print "You can legally buy alcohol."
elif int(user_age) < 21:
    print "You cannot buy alcohol."

#user_name1 = raw_input("Enter your name: ")
user_bmonth = raw_input("Enter the month you were born: ")
user_bday = raw_input("Enter the day you were born: ")
current_month = 7
current_day = 9
if int(user_bmonth) > int(current_month) and int(user_bday) > int(current_day):
    print "Your birthday is in", int(user_bmonth) - int(current_month), "month(s) and", int(user_bday)-int(current_day), "day(s)!"
if int(user_bmonth) < int(current_month) and int(user_bday) > int(current_day):
    print "Your birthday is in", 12 - (int(current_month) - int(user_bmonth)), "month(s) and", int(user_bday) - int(
        current_day), "day(s)!"
if int(user_bmonth) < int(current_month) and int(user_bday) < int(current_day):
    print "Your birthday is in", 12- (int(current_month) - int(user_bmonth)), "month(s) and", 30 - (int(current_day) - int(
        user_bday)) + (12- (int(current_month) - int(user_bmonth))) - 1, "day(s)!"
if int(user_bmonth) > int(current_month) and int(user_bday) < int(current_day):
    print "Your birthday is in", int(user_bmonth) - int(current_month), "month(s) and", 30 - (int(current_day) - int(
        user_bday)) + (int(user_bmonth) - int(current_month))- 1, "day(s)!"
if int(user_bmonth) == int(current_month) and int(user_bday) < int(current_day):
    print "Your birthday is in 11 months and", 30 - (int(current_day) - int(
        user_bday)) + (int(user_bmonth) - int(current_month))- 1, "day(s)!"
#user_age1 = raw_input("Enter your age: ")

