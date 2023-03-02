# Python Program to Find the Sum of Digits in a Number

num = int(input("Enter any Number : "))
num1 = num
sum = 0

'''
num1 = str(num)
for i in range(0,len(num1)):
    sum = sum + int(num1[i])
'''

while(num1>0):
    # print(num1)
    sum = sum + num1%10
    # print(sum)
    num1 = num1//10
    # print(num1)
    # print()

print("The total sum of digits of {} is {}.".format(num,sum))