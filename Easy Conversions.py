#decimal to binary or octal
dnum=int(input())
bnum=''
while dnum!=0:
    rem=dnum%2
    bnum=bnum+str(rem)
    dnum//=2             #change 2 to 8 to ur needs
print(bnum[::-1])


#Binary to decimal
bnum=input()
bnum=bnum[::-1]
s=0
for i in range(len(bnum)):
    number=int(bnum[i])
    power=i
    s+=number*2**power
print(s)












