# Curzon Numbers
# In this challenge, establish if a given integer num is a Curzon number. 
# If 1 plus 2 elevated to num is exactly divisible 
# by 1 plus 2 multiplied by num, then num is a Curzon number.

# Given a non-negative integer num, 
# implement a function that returns True 
# if num is a Curzon number, or False otherwise.

# Examples
# is_curzon(5) ➞ True
# # 2 ** 5 + 1 = 33
# # 2 * 5 + 1 = 11
# # 33 is a multiple of 11

# is_curzon(10) ➞ False
# # 2 ** 10 + 1 = 1025
# # 2 * 10 + 1 = 21
# # 1025 is not a multiple of 21

# is_curzon(14) ➞ True
# # 2 ** 14 + 1 = 16385
# # 2 * 14 + 1 = 29
# # 16385 is a multiple of 29

def is_curzon(number):
    power2 = 2 ** number + 1
    multiply2 = 2 * number + 1
    if power2 % multiply2 == 0:
        print(f"Number {number} is a curzon number")
    else:
        print(f"Number {number} is not a curzon number")
is_curzon(5) 
is_curzon(10)
is_curzon(14) 
