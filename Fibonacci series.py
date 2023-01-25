n=int(input("Enter a number"))
print("Fibonacci series is: ",end='')
a,b=-1,1
for i in  range(n):
    c=a+b
    print(c,end=',')
    a,b=b,c
