# Python Program to Read a Mumber n and Compute n+nn+nnn

n = int(input("Enter any number : "))

t1 = str(n)
t2 = int(t1+t1)
t3 = int(t1+t1+t1)
ans = n+t2+t3
print("The Value of {}+{}+{} : {}".format(n,t2,t3,ans))
