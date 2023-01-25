x=int(input('''\n1-Area of a circle 1 
\n2-Perimeter of a circle 2
\n3-Exit 3
\nEnter Your desired option(Number).''')) #x=Selector.

#Area of Circle

if x==1:
    r=float(input("Enter the radius of the circle in cm."))
    print("The area of the circle with radius",r,"cm is",(3.14*r*r))
    
#Perimeter of circle
    
elif x==2:
    r=float(input("Enter the radius of the circle in cm."))
    print("The perimeter of the circle with radius",r,"cm is",(2*3.14*r))
    
#ExIt, ExIt NoW:

elif x==3:
    print("Come back later!")
