# Python Program to test Collatz Conjecture for a Given Number
'''
• The Collatz conjecture is a conjecture that a particular sequence 
always reaches 1. The sequence is defined as: start with a 
number n. The next number in the sequence is n/2 if n is even and 
3n + 1 if n is odd.
• Examples. For instance, starting with n = 12, one gets the 
sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1. n = 19, for example, takes 
longer to reach 1: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 
40, 20, 10, 5, 16, 8, 4, 2, 1
'''

num = int(input("Enter the starting term : "))

print("Collatz Conjecture for given number : ")

while(num!=1):
    print(int(num),end=",")
    if num%2==0:
        num = num/2
    else:
        num = num*3 + 1

print(1,end="")
