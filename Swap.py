# Python Program to Exchange the Values of Two Numbers Without Using a 
# Temporary Variable

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

# print("After Swaping, Value of 1st Number is {} and value  of 2nd Number is {}.".format(num1,num2))
print("Value of 1st Number : {} \nValue of 2nd Number is : {}".format(num1,num2))