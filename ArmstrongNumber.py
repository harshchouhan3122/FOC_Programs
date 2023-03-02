# Python Program to Check if a Number is an Armstrong Number
'''
• Armstrong number is a number that is 
equal to the sum of cubes of its digits. For 
example 0, 1, 153, 370, 371 and 407 are 
the Armstrong numbers.
• For a 4 digit number, every digit would be 
raised to their fourth power to get the 
desired result. 1634, 8208, 9474 are a few 
examples of a 4 digit armstrong number
'''
import math

num = int(input("Enter any number : "))
numstr = str(num)

numlen = len(str(num))
# print(numlen)

sum = 0

for i in numstr:
    sum = sum + math.pow(int(i),numlen)

if sum == num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")