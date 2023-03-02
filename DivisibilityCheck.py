# Python Program to Print all Integers that Aren’t Divisible by 
# Either 2 or 3 and Lie between 1 and 50

print("The Number from 0 to 50 which are not divisible by 2 and 3 are :")

low = 1
up = 50
num1 = 2
num2 = 3

for i in range (low,up+1):
    if i%num1!=0 and i%num2!=0:
        print(i)

