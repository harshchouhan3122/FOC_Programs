'''
# Python Program to Check if a Number is a Palindrome

num = int(input("Enter any number : "))

org = num
rev = 0

while(num>0):
    rev = (rev*10) + num%10
    num = num//10

if org == rev:
    ans = "Palindrome Number."
else:
    ans = "Not a Palindrome Number."

print(ans)
'''

# Check the Palindrome String
str1 = str(input("Enter String : ")).lower()
revstr = ""

revstr = str1[::-1]

if str1 == revstr:
    print("Palindrome")
else:
    print("Not a Palindrome")