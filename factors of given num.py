n=int(input("Enter a number i'll find it's factors: "))
for i in range(1,n+1):
    if(n%i==0):
        print(i,sep=",",end=' ')
