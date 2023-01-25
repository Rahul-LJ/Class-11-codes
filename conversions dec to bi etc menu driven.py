#conversions of python numbers using menu driven

n=int(input('Menu Driven code \n1)Decimal to binary \n2)Binary to decimal \n3)decimal to octal \n4)Exit \nChoose your dezired conversion:'))
if n==1:
    dnum=int(input('Enter decimal number: '))
    i=0
    bnum=[]
    while dnum!=0:
        rem=dnum%2
        bnum.insert(i,rem)
        i+=1
        dnum=int(dnum/2)
    i-=1
    print('\nEquavalant binary value is: ')
    while i>=0:
        print(end=str(bnum[i]))
        i-=1
    print()

elif n==2:
    bnum=int(input('Enter binary number; '))
    dnum=0
    i=1
    while bnum!=0:
        rem=bnum%10
        dnum+=rem*i
        i*=2
        bnum=bnum//10
    print('Equavalant decimal value is ',dnum)

elif n==3:
    dnum=int(input('enter decimal number: '))
    i=0
    onum=[]
    while dnum!=0:
        rem=dnum%8
        onum.insert(i,rem)
        i+=1
        dnum=dnum//2
    i-=1
    print('Equavalant octal value is ')
    while i>=0:
        print(end=str(onum[i]))
        i-=1
    print()

elif n==4:
    print('Exited, restart the code to run again.')

else:
    print('invalid input, try again next time.')
