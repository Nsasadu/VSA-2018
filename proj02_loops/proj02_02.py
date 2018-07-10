# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
# key word is for
# loop over a range of #s
# loop over strings

# s = "vsa"
# for letter in s:
#     print letter
#     if letter == "s":
#         print "This is an s"
#
# sum = 0
# for num in range (0,9):
#     sum = sum + num
#     print sum


# sum = 0
# num_low = 0
# num_high = 1
# num_spare = 0
# user_fibonacci = raw_input("How many Fibonacci numbers would you like to generate? ")
# print 1
# for num in range(int(user_fibonacci) - 1):
#     print num_high + num_low
#     num_spare = num_high
#     num_high = num_low + num_high
#     num_low = num_spare


sum = 0
num_low2 = 2
num_high2 = 3
num_spare2 = 4
user_power = raw_input("How many powers of two would you like to generate? ")
print 2
for num in range(int(user_power) - 1):
    print 2 ** num_low2
    num_spare2 = num_high2
    num_high2 = num_low2 + num_high2
    num_low2 = num_spare2