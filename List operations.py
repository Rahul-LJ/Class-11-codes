n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))
large=l[0]
for i in range(n):
    if l[i]>large:
        large=l[i]
for i in range(n):
    if l[i]!=large:
        sec=l[i]
        break
for i in range(n):
    if l[i]!=large and l[i]>sec:
        sec=l[i]
print("Largest is:",large)
print("Second largest is:",sec)
#__________________________________

least=l[0]
for i in range(n):
    if l[i]<least:
        least=l[i]
for i in range(n):
    if l[i]!=least:
        sec=l[i]
        break
for i in range(n):
    if l[i]!=least and l[i]<sec:
        sec=l[i]
print("Least is:",least)
print("Second least is:",sec)
