l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))
for i in range(l,u+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=",")
print("are the prime numbers in this range")
        
