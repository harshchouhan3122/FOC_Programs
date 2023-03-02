# Python Program to Reverse a Given Number

num = int(input("Enter any number : "))

orgNum = num
revNum = 0

 # 124 = 421

while(num>0):
    revNum = (revNum*10) + num%10
    num = num//10

print("Reverse of {} is {}.".format(orgNum,revNum))
   
