#!/usr/bin/python

import cmath



#(-b + sqrt(b^2 - 4AC))/2a
   
print("Welcome to the Quadratic Formula Calculator")
print("In the format ax^2 + bx + c = 0")   
A = eval(raw_input("What is your Value for A?"))
B = eval(raw_input("What is your Value for B?"))
C = eval(raw_input("What is your Value for C?"))

D = B**2-4*A*C # discriminant

if D < 0:
    print ("This equation has no real solution")
elif D == 0:
    x = (-B+math.sqrt(B**2-4*A*C))/2*A
    print ("This equation has one solutions: "), x
else:
    x1 = (-B+math.sqrt((B**2)-(4*(A*C))))/(2*A)
    x2 = (-B-math.sqrt((B**2)-(4*(A*C))))/(2*A)
    print ("This equation has two solutions: ", x1, " or", x2)