#Converting seconds to h:m:s
s=int(input("Enter time in seconds:"))
h=s%86400//3600
m=s%3600//60
sec=s%60
print("your time is:",h,":",m,":",sec)
#converting h:m:s to seconds
a=int(input("Enter hours:"))
b=int(input("Enter Minutes:"))
c=int(input("Enter seconds:"))
seconds=a*3600+b*60+c
print("The h:m:s converted to seconds is:",seconds)



