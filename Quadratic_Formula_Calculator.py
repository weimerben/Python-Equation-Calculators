#!/usr/bin/python

import cmath



#(-b + sqrt(b^2 - 4AC))/2a
   
print("Welcome to the Quadratic Formula Calculator")
print("In the format ax^2 + bx + c = 0")   
A = eval(raw_input("What is your Value for A?"))
B = eval(raw_input("What is your Value for B?"))
C = eval(raw_input("What is your Value for C?"))

x1 = ((-B - cmath.sqrt(B ** 2 - 4*A*C))/(2*A))
x2 = ((-B + cmath.sqrt(B ** 2 - 4*A*C))/(2*A))

print(x1)
print("or")
print(x2)