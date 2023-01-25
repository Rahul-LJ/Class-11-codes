n=int(input('Enter a number to know its factorial: '))


f=1            #since if u put 0 then output will always be zero


for i in range(1,n+1):
    f*=i
print('The factorial of ',n,'is ',f)
    
