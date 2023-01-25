#triangle type
int(input("Enter to know your type of triangle!"))
a=float(input("Enter the first side of the triangle:"))
b=float(input("Enter the second side of the triangle:"))
c=float(input("Enter the third side of the triangle:"))
if a==b and b==c:
    print("Its an equilateral triangle")
elif a==b or b==c or c==a:
    print("Its an isosceles triangle")
else:
    print("Its a scalene triangle")
