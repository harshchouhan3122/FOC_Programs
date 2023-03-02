# Python Program to Read a Number n And Print the Series 
# "1+2+…..+n= "

num = int(input("Enter any number : "))
series = []
sum = 0

for i in range(1,num+1):
    series.append(str(i))
    sum = sum + i

print(" + ".join(series),"=",sum)   #.join work only on the string datatypes of list

