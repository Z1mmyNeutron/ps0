import numpy
print("Hi welcome")
x = int(input("Insert a number for x:"))
y = int(input("Insert a number for y:"))
print(x ** y)
if(x > 0):
    print(numpy.log2(x))
else: 
    print("Logarithm is only defined for positive numbers")
