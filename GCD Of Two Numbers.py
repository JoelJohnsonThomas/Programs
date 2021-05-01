# finding GCD of two numbers
a = int(input("enter the number:"))
b = int(input("enter another number:"))
rem = a % b
while rem !=0:
    a = b
    b = rem
    rem = a % b
print("The given GCD number :",b)
    
