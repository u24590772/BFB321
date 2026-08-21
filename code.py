from math import sqrt

a=input("Enter the value of a: ")
b=input("Enter the value of b: ")
c=input("Enter the value of c: ")

a=float(a)
b=float(b)
c=float(c)

y=(sqrt(b**2-4*a*c))/(2*a)
print("The value of y is:", y)

