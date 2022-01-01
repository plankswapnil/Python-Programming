#Calculating the area of triangle using heron's formula with python
#Taking input from user
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
#Declaring semiparimeter
s=(a+b+c)/2
#Appyling heron's formula to calculate the area of triangle
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of triangle is %0.2f"%area)