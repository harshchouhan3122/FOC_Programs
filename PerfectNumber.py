# Python Program to Check if a Number is a Perfect Number

'''
Perfect number, a positive integer 
that is equal to the sum of its proper 
divisors. The smallest perfect 
number is 6, which is the sum of 1, 
2, and 3. Other perfect numbers are 
28, 496, and 8,128
'''

num = int(input("Enter any Number : "))
sum = 0

'''
factor = []

for i in range(1,num):
    if num%i==0:
        factor.append(i)

# print(factor)

for i in factor:
    sum = sum + i

'''

# '''
for i in range(1,num):
    if num%i==0:
        sum = sum + i
# '''

if num == sum :
    ans = "Perfect Number"
else:
    ans = "Not a Perfect Number"

print(ans)


    