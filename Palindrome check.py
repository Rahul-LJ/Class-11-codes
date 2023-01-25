s=input('Enter a string to check if its a palindrome: ')
a=s.upper()
if a[::]==a[::-1]:
    print('Its a palindrome')
else:
    print('Its not a palindrome')

#for integer_____________________________

'''n=int(input('Enter a number to check if its palindrome: '))
rem=0
rev=0
num=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
    if rev == n:
        print('its a palindrome')
    else:
        print('It\'s not a palindrome')''' #error
