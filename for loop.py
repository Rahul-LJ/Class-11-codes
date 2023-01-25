'''n=int(input('Enter a number > 20 :'))
for k in range(n):
    for j in range(n):
        for r in range(j+1):
            print('# ',end='')
        print()

    for a in range(n):
        for b in range(n-a):
            print('# ',end='')
        print()'''
1234
123
12
1

for i in range(1,5):
    for j in range(i,5):
        print(j-(i-1),end='')
    print()
