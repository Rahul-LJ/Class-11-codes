print("Let's check if a number is leap year or not!")
n=int(input("Enter year:"))
if n%4==0:
    if n%400==0:
        if n%100==0:
            print("Its a leap year")
        else:
            print("Its not a leap year")
    else:
        print("Its not a leap year")
else:
    print("Its not a leap year")
