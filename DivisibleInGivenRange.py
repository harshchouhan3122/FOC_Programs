# Python Program to Print all Numbers in a Range 
# Divisible by a Given Number

lowerRange = int(input("Enter the starting Number : "))
upperRange = int(input("Enter the ending Number : "))

num = int(input("Enter the divisor : "))

for i in range(lowerRange,upperRange+1):
    if i%num==0:
        print(i)