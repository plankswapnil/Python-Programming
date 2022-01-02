#program to swap two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
 
#use temporary variable to swap two numbers.
temp = a
a = b
b = temp
 
print("The value of a and b after swapping is {} and {}".format(a,b))
