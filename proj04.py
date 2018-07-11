# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

value = []
counter = 0
valuea = list(set(a))
for item in a:
    if item < 5:
        value.append(valuea[counter])
        counter = counter + 1
print value





#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # and write a program that creates and prints a list that contains only the elements
# # that are common between the lists (without duplicates).
# # Make sure your program works on two lists of different sizes.
#
#
valuebc = []
counter = 0
valueb = list(set(b))
valuec = list(set(c))
for item in valueb:
    if item in c:
        valuebc.append(valueb[counter])
    counter = counter + 1
print valuebc


import random
list1 = []
list2 = []
list3 = []
counter = 0
listlength = random.randint(1,20)
while counter < listlength:
    num1 = random.randint(1,50)
    list1.append(num1)
    counter = counter + 1
print "List 1 values", list1

counter = 0
listlength = random.randint(1,20)
while counter < listlength:
    num2 = random.randint(1,50)
    list2.append(num2)
    counter = counter + 1
print "List 2 values", list2

counter = 0
value1 = list(set(list1))
value2 = list(set(list2))
for item in value1:
    if item in value2:
        list3.append(value1[counter])
    counter = counter + 1
print list3

#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.

# counter = 0
# for item in d:
#     if item == "a":
#         d[counter] = "*"
#     counter = counter + 1
# print d

# var = []
# var2 = [7, 2, 3, "cat", "a", "b"]
#
# # index - 0 indexed
# # one item
# print var2[3]
# # slice of list
# print var2[0:4]
# # all but first
# print var2[1:]
# # all but last
# print var2[:-1]
#
# # replace
# var2[0] = "tree"
# print var2
#
#
# # loop
# # to change
# counter = 0
# for item in var2:
#     if item == "cat":
#         var2[counter] = "dog"
#     elif item == "tree":
#         var2[counter] = "flower"
#     counter = counter + 1
# print var2
#
# var2.append("I like turtles")
# print var2
#
# lst = []
# s= "This is a string"
# for letter in s:
#     lst.append(letter)
# print lst

#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

counter = 0
counter1 = 0
user_string = raw_input("Enter a phrase to see if it is a palindrome or not: ")
user_string = user_string.lower()
user_lst = []
length = int(len(user_lst))
for item in user_lst:
    if item == " ":
        user_lst[counter1] = ""
for letter in user_string:
    user_lst.append(letter)
if user_lst[0] != user_lst[-1]:
    print "This word is not a palindrome."
    exit()
while counter < length:
    if user_lst[0] == user_lst[-1]:
        user_lst == user_lst[1:-1]
        counter = counter + 1
while counter >= length:
    if user_lst[0] == user_lst[-1]:
        print "This word is a palindrome!"
        break

