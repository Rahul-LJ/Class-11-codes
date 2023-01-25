#matrix
m=int(input('Enter no.of rows:'))
n=int(input('Enter no.of columns:'))
matrix=[]
print('Enter elements')
for i in range(m):
    l=[]
    for i in range(n):
        l.append(int(input('')))
    matrix.append(l)
    
#to print matrix
    
for i in range(m):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print('')
    
