n=int(input('Enter no.of elements: '))
l=[]
for i in range(n):
    l.append(int(input('Enter the number: ')))
for i in range(len(l)-1):
        
        if l[i]>l[i+1]:

            l[i] = l[i+1]
            l[i+1] = l[i]
print(l)
